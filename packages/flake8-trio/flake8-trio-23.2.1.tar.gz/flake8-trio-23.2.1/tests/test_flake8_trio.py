"""Main test file for the plugin."""

from __future__ import annotations

import ast
import copy
import itertools
import os
import re
import site
import subprocess  # noqa: S404
import sys
import tokenize
import unittest
from collections import deque
from pathlib import Path
from typing import TYPE_CHECKING, Any, DefaultDict

import pytest
from flake8 import __version_info__ as flake8_version_info
from flake8.options.manager import OptionManager
from hypothesis import HealthCheck, given, settings
from hypothesmith import from_grammar, from_node

from flake8_trio import Plugin
from flake8_trio.base import Error, Statement
from flake8_trio.visitors import ERROR_CLASSES

if TYPE_CHECKING:
    from collections.abc import Iterable, Sequence


test_files: list[tuple[str, Path]] = sorted(
    (f.stem.upper(), f) for f in (Path(__file__).parent / "eval_files").iterdir()
)


class ParseError(Exception):
    ...


# flake8 6 added a required named parameter formatter_names
def _default_option_manager():
    kwargs = {}
    if flake8_version_info[0] >= 6:
        kwargs["formatter_names"] = ["default"]
    return OptionManager(version="", plugin_versions="", parents=[], **kwargs)


# check for presence of _pyXX, skip if version is later, and prune parameter
def check_version(test: str):
    python_version = re.search(r"(?<=_PY)\d*", test)
    if python_version:
        version_str = python_version.group()
        major, minor = version_str[0], version_str[1:]
        v_i = sys.version_info
        if (v_i.major, v_i.minor) < (int(major), int(minor)):
            pytest.skip(f"python version {v_i} smaller than {major}, {minor}")


ERROR_CODES = {
    err_code: err_class
    for err_class in ERROR_CLASSES
    for err_code in err_class.error_codes.keys()
}


@pytest.mark.parametrize(("test", "path"), test_files)
def test_eval(test: str, path: Path):
    # version check
    check_version(test)
    test = test.split("_")[0]

    parsed_args = []

    # only enable the tested visitor to save performance and ease debugging
    # if a test requires enabling multiple visitors they specify a
    # `# ARG --enable-vis...` that comes later in the arg list, overriding this
    if test in ERROR_CODES:
        parsed_args = [f"--enable-visitor-codes-regex={test}"]

    expected: list[Error] = []

    with open(path, encoding="utf-8") as file:
        lines = file.readlines()

    for lineno, line in enumerate(lines, start=1):
        # interpret '\n' in comments as actual newlines
        line = line.replace("\\n", "\n")

        line = line.strip()

        # add command-line args if specified with #ARG
        if reg_match := re.search(r"(?<=ARG ).*", line):
            parsed_args.append(reg_match.group().strip())

        # skip commented out lines
        if not line or line[0] == "#":
            continue

        # get text between `error:` and (end of line or another comment)
        k = re.findall(r"(error|TRIO...):([^#]*)(?=#|$)", line)

        for err_code, err_args in k:
            try:
                # Append a bunch of empty strings so string formatting gives garbage
                # instead of throwing an exception
                try:
                    args = eval(  # noqa: S307
                        f"[{err_args}]",
                        {
                            "lineno": lineno,
                            "line": lineno,
                            "Statement": Statement,
                            "Stmt": Statement,
                        },
                    )
                except NameError:
                    print(f"failed to eval on line {lineno}", file=sys.stderr)
                    raise

            except Exception as e:
                print(f"lineno: {lineno}, line: {line}", file=sys.stderr)
                raise e

            if args:
                col, *args = args
            else:
                col = 0
            assert isinstance(
                col, int
            ), f"invalid column {col!r} @L{lineno}, in {line!r}"

            if err_code == "error":
                err_code = test
            error_class = ERROR_CODES[err_code]
            message = error_class.error_codes[err_code]
            try:
                expected.append(Error(err_code, lineno, int(col), message, *args))
            except AttributeError as e:
                msg = (
                    f"Line {lineno}: Failed to format\n {message!r}\n" f'"with\n{args}'
                )
                raise ParseError(msg) from e

    assert parsed_args, "no parsed_args"
    assert expected, f"failed to parse any errors in file {path}"

    plugin = Plugin.from_filename(path)
    assert_expected_errors(plugin, *expected, args=parsed_args)


# Codes that are supposed to also raise errors when run on sync code, and should
# be excluded from the SyncTransformer check.
# Expand this list when adding a new check if it does not care about whether the code
# is asynchronous or not.
error_codes_ignored_when_checking_transformed_sync_code = {
    "TRIO100",
    "TRIO101",
    "TRIO103",
    "TRIO104",
    "TRIO105",
    "TRIO106",
    "TRIO111",
    "TRIO112",
    "TRIO115",
    "TRIO116",
    "TRIO117",
}


class SyncTransformer(ast.NodeTransformer):
    def visit_Await(self, node: ast.Await):
        return self.generic_visit(node.value)

    def replace_async(self, node: ast.AST, target: type[ast.AST]) -> ast.AST:
        node = self.generic_visit(node)
        newnode = target()
        newnode.__dict__ = node.__dict__
        return newnode

    def visit_AsyncFunctionDef(self, node: ast.AST):
        return self.replace_async(node, ast.FunctionDef)

    def visit_AsyncWith(self, node: ast.AST):
        return self.replace_async(node, ast.With)

    def visit_AsyncFor(self, node: ast.AST):
        return self.replace_async(node, ast.For)


@pytest.mark.parametrize(("test", "path"), test_files)
def test_noerror_on_sync_code(test: str, path: Path):
    if any(e in test for e in error_codes_ignored_when_checking_transformed_sync_code):
        return
    with tokenize.open(path) as f:
        source = f.read()
    tree = SyncTransformer().visit(ast.parse(source))

    ignored_codes_regex = (
        "(?!("
        + "|".join(error_codes_ignored_when_checking_transformed_sync_code)
        + "))"
    )
    assert_expected_errors(
        Plugin(tree),
        args=[f"--enable-visitor-codes-regex={ignored_codes_regex}"],
    )


def initialize_options(plugin: Plugin, args: list[str] | None = None):
    om = _default_option_manager()
    plugin.add_options(om)
    plugin.parse_options(om.parse_args(args=(args if args else [])))


def assert_expected_errors(
    plugin: Plugin,
    *expected: Error,
    args: list[str] | None = None,
):
    # initialize default option values
    initialize_options(plugin, args)

    errors = sorted(e for e in plugin.run())
    expected_ = sorted(expected)

    print_first_diff(errors, expected_)
    assert_correct_lines_and_codes(errors, expected_)
    assert_correct_columns(errors, expected_)
    assert_correct_args(errors, expected_)

    # full check
    assert errors == expected_

    # test tuple conversion and iter types
    assert_tuple_and_types(errors, expected_)


def print_first_diff(errors: Sequence[Error], expected: Sequence[Error]):
    first_error_line: list[Error] = []
    first_expected_line: list[Error] = []
    for err, exp in zip(errors, expected):
        if err == exp:
            continue
        if not first_error_line or err.line == first_error_line[0]:
            first_error_line.append(err)
        if not first_expected_line or exp.line == first_expected_line[0]:
            first_expected_line.append(exp)

    if first_expected_line != first_error_line:
        print(
            "\nFirst lines with different errors",
            f"  actual: {[e.cmp() for e in first_error_line]}",
            f"expected: {[e.cmp() for e in first_expected_line]}",
            "",
            sep="\n",
            file=sys.stderr,
        )


def assert_correct_lines_and_codes(errors: Iterable[Error], expected: Iterable[Error]):
    MyDict = DefaultDict[int, DefaultDict[str, int]]
    # Check that errors are on correct lines
    all_lines = sorted({e.line for e in (*errors, *expected)})
    error_dict: MyDict = DefaultDict(lambda: DefaultDict(int))
    expected_dict = copy.deepcopy(error_dict)

    for e in errors:
        error_dict[e.line][e.code] += 1
    for e in expected:
        expected_dict[e.line][e.code] += 1

    any_error = False
    for line in all_lines:
        if error_dict[line] == expected_dict[line]:
            continue
        for code in sorted({*error_dict[line], *expected_dict[line]}):
            if not any_error:
                print(
                    "Lines with different # of errors:",
                    "-" * 38,
                    f"| line | {'code':7} | actual | expected |",
                    sep="\n",
                    file=sys.stderr,
                )
                any_error = True

            print(
                f"| {line:4}",
                f"{code}",
                f"{error_dict[line][code]:6}",
                f"{expected_dict[line][code]:8} |",
                sep=" | ",
                file=sys.stderr,
            )
    assert not any_error


def assert_correct_columns(errors: Iterable[Error], expected: Iterable[Error]):
    # check errors have correct columns
    col_error = False
    for err, exp in zip(errors, expected):
        assert err.line == exp.line
        if err.col != exp.col:
            if not col_error:
                print("Errors with same line but different columns:", file=sys.stderr)
                print("| line | actual | expected |", file=sys.stderr)
                col_error = True
            print(
                f"| {err.line:4} | {err.col:6} | {exp.col:8} |",
                file=sys.stderr,
            )
    assert not col_error


def assert_correct_args(errors: Iterable[Error], expected: Iterable[Error]):
    # check errors have correct messages
    args_error = False
    for err, exp in zip(errors, expected):
        assert (err.line, err.col, err.code) == (exp.line, exp.col, exp.code)
        if err.args != exp.args:
            if not args_error:
                print(
                    "Errors with different args:",
                    "-" * 20,
                    sep="\n",
                    file=sys.stderr,
                )
                args_error = True
            print(
                f"*    line: {err.line:3} differs\n",
                f"  actual: {err.args}\n",
                f"expected: {exp.args}\n",
                "-" * 20,
                file=sys.stderr,
            )
    assert not args_error


def assert_tuple_and_types(errors: Iterable[Error], expected: Iterable[Error]):
    def info_tuple(error: Error):
        try:
            return tuple(error)
        except IndexError:
            print(
                "Failed to format error message",
                f"line: {error.line}",
                f"col: {error.col}",
                f"code: {error.code}",
                f"args: {error.args}",
                f"format string: {ERROR_CODES[error.code].error_codes[error.code]!r}",
                sep="\n    ",
                file=sys.stderr,
            )
            raise

    for err, exp in zip(errors, expected):
        err_msg = info_tuple(err)
        for err, type_ in zip(err_msg, (int, int, str, type(None))):
            assert isinstance(err, type_)
        assert err_msg == info_tuple(exp)


def test_107_permutations():
    """Tests all possible permutations for TRIO107.

    Since each test is so fast, and there's so many permutations, manually doing
    the permutations in a single test is much faster than the permutations from using
    pytest parametrization - and does not clutter up the output massively.

    generates code that looks like this, where a block content of `None` means the
    block is excluded:

    async def foo():
        try:
            await foo() | ...
        except ValueError:
            await foo() | ... | raise | return | None
        except SyntaxError:
            await foo() | ... | raise | return | None
        except:
            await foo() | ... | raise | return | None
        else:
            await foo() | ... | return | None
        finally:
            await foo() | ... | return | None
    """
    plugin = Plugin(ast.AST())
    initialize_options(plugin, args=["--enable-visitor-codes-regex=TRIO107"])

    check = "await foo()"

    # loop over all the possible content of the different blocks
    for try_, exc1, exc2, bare_exc, else_, finally_ in itertools.product(
        (check, "..."),  # try_
        (check, "...", "raise", "return", None),  # exc1
        (check, "...", "raise", "return", None),  # exc2
        (check, "...", "raise", "return", None),  # bare_exc
        (check, "...", "return", None),  # else_
        (check, "...", "return", None),  # finally_
    ):
        # exclude duplicate tests where there's a second exception block but no first
        if exc1 is None and exc2 is not None:
            continue

        # syntax error if there's no exception block but there's finally and/or else
        if exc1 is exc2 is bare_exc is None and (finally_ is None or else_ is not None):
            continue

        function_str = f"async def foo():\n  try:\n    {try_}\n"

        for arg, val in {
            "except ValueError": exc1,
            "except SyntaxError": exc2,
            "except": bare_exc,
            "else": else_,
            "finally": finally_,
        }.items():
            if val is not None:
                function_str += f"  {arg}:\n    {val}\n"

        tree = ast.parse(function_str)

        # not a type error per se, but it's pyright warning about assigning to a
        # protected class member - hence we silence it with a `type: ignore`.
        plugin._tree = tree  # type: ignore
        errors = list(plugin.run())

        if (
            # return in exception
            "return" in (exc1, exc2, bare_exc)
            # exception and finally doesn't checkpoint, checkpoint in try might not run
            or ("..." in (exc1, exc2, bare_exc) and finally_ != check)
            # no checkpoints in normal control flow
            or check not in (try_, finally_, else_)
            # return in else|finally w/o checkpoint before
            or ("return" in (else_, finally_) and check not in (else_, try_))
            # return in finally with no bare exception, checkpoint in try might not run
            or (finally_ == "return" and bare_exc is None)
        ):
            assert errors, "# missing alarm:\n" + function_str
        else:
            assert not errors, "# false alarm:\n" + function_str


def test_114_raises_on_invalid_parameter(capsys: pytest.CaptureFixture[str]):
    plugin = Plugin(ast.AST())
    # flake8 will reraise ArgumentError as SystemExit
    for arg in "blah.foo", "foo*", "*":
        with pytest.raises(SystemExit):
            initialize_options(plugin, args=[f"--startable-in-context-manager={arg}"])
        out, err = capsys.readouterr()
        assert not out
        assert f"{arg!r} is not a valid method identifier" in err


def test_200_options(capsys: pytest.CaptureFixture[str]):
    plugin = Plugin(ast.AST())
    for i, arg in (0, "foo"), (2, "foo->->bar"), (2, "foo->bar->fee"):
        with pytest.raises(SystemExit):
            initialize_options(plugin, args=[f"--trio200-blocking-calls={arg}"])
        out, err = capsys.readouterr()
        assert not out, out
        assert all(word in err for word in (str(i), arg, "->"))


def _test_trio200_from_config_common(tmp_path: Path) -> str:
    tmp_path.joinpath(".flake8").write_text(
        """
[flake8]
trio200-blocking-calls =
  other -> async,
  sync_fns.* -> the_async_equivalent,
select = TRIO200
"""
    )
    tmp_path.joinpath("example.py").write_text(
        """
import sync_fns

async def foo():
    sync_fns.takes_a_long_time()
"""
    )
    return (
        "./example.py:5:5: TRIO200 User-configured blocking sync call sync_fns.* "
        "in async function, consider replacing with the_async_equivalent.\n"
    )


def test_200_from_config_flake8_internals(
    tmp_path: Path, capsys: pytest.CaptureFixture[str]
):
    # abuse flake8 internals to avoid having to use subprocess
    # which breaks breakpoints and hinders debugging
    # TODO: fixture (?) to change working directory

    err_msg = _test_trio200_from_config_common(tmp_path)
    # replace ./ with tmp_path/
    err_msg = str(tmp_path) + err_msg[1:]

    from flake8.main.cli import main

    main(
        argv=[
            str(tmp_path / "example.py"),
            "--append-config",
            str(tmp_path / ".flake8"),
        ]
    )
    out, err = capsys.readouterr()
    assert not err
    assert err_msg == out


def test_200_from_config_subprocess(tmp_path: Path):
    err_msg = _test_trio200_from_config_common(tmp_path)
    res = subprocess.run(  # noqa: S603,S607
        ["flake8"], cwd=tmp_path, capture_output=True
    )
    assert not res.stderr
    assert res.stdout == err_msg.encode("ascii")


def test_900_default_off(capsys: pytest.CaptureFixture[str]):
    from flake8.main.cli import main

    main(
        argv=[
            "tests/trio900.py",
        ]
    )
    out, err = capsys.readouterr()
    assert not err
    assert "TRIO900" not in out


# from https://docs.python.org/3/library/itertools.html#itertools-recipes
def consume(iterator: Iterable[Any]):
    deque(iterator, maxlen=0)


@pytest.mark.fuzz()
class TestFuzz(unittest.TestCase):
    @settings(max_examples=1_000, suppress_health_check=[HealthCheck.too_slow])
    @given((from_grammar() | from_node()).map(ast.parse))
    def test_does_not_crash_on_any_valid_code(self, syntax_tree: ast.AST):
        # TODO: figure out how to get unittest to play along with pytest options
        # so `--enable-visitor-codes-regex` can be passed through.
        # Though I barely notice a difference manually changing this value, or even
        # not running the plugin at all, so overhead looks to be vast majority of runtime
        enable_visitor_codes_regex = ".*"

        # Given any syntatically-valid source code, the checker should
        # not crash.  This tests doesn't check that we do the *right* thing,
        # just that we don't crash on valid-if-poorly-styled code!
        plugin = Plugin(syntax_tree)
        initialize_options(
            plugin, [f"--enable-visitor-codes-regex={enable_visitor_codes_regex}"]
        )

        consume(plugin.run())


def _iter_python_files():
    # Because the generator isn't perfect, we'll also test on all the code
    # we can easily find in our current Python environment - this includes
    # the standard library, and all installed packages.
    for base in sorted(set(site.PREFIXES)):
        for dirname, _, files in os.walk(base):
            for f in files:
                if f.endswith(".py"):
                    yield Path(dirname) / f


@pytest.mark.fuzz()
def test_does_not_crash_on_site_code(enable_visitor_codes_regex: str):
    for path in _iter_python_files():
        try:
            plugin = Plugin.from_filename(str(path))
            initialize_options(
                plugin, [f"--enable-visitor-codes-regex={enable_visitor_codes_regex}"]
            )
            consume(plugin.run())
        except Exception as err:
            raise AssertionError(f"Failed on {path}") from err
