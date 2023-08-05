import sys
import traceback
from fnmatch import fnmatch
from io import StringIO
from itertools import zip_longest
from pathlib import Path
from typing import IO, AnyStr, List, Optional

from click.testing import Result
from pynmrstar import Entry
from typer import Typer
from typer.testing import CliRunner

NOQA_E501 = "# noqa: E501"


def run_and_read_pytest(args):

    from pytest import main

    original_output = sys.stdout
    original_error = sys.stdout
    sys.stdout = StringIO()
    sys.stderr = StringIO()

    retcode = main(args)

    output = sys.stdout.getvalue()
    error_output = sys.stderr.getvalue()

    sys.stdout.close()
    sys.stderr.close()
    sys.stdout = original_output
    sys.stderr = original_error

    return retcode, output, error_output


def _split_test_spec(spec):
    spec_parts = spec.split("::")
    spec_parts[0] = Path(spec_parts[0])

    return spec_parts


def select_matching_tests(tests, selectors):
    results = []

    for selector in selectors:

        selector_parts = _split_test_spec(selector)
        num_selector_parts = len(selector_parts)

        if num_selector_parts == 1:
            selector = f"*::{selector_parts[0]}"
            selector_parts = _split_test_spec(selector)
            num_selector_parts = len(selector_parts)

        if num_selector_parts == 2 and selector_parts[0] == Path(""):
            selector = f"*::{selector_parts[1]}"
            selector_parts = _split_test_spec(selector)
            num_selector_parts = len(selector_parts)

        if num_selector_parts == 2 and selector_parts[1] == "":
            selector = f"{selector_parts[0]}::*"
            selector_parts = _split_test_spec(selector)
            num_selector_parts = len(selector_parts)

        selector_path_parts = selector_parts[0].parts
        num_selector_path_parts = len(selector_path_parts)

        for test in tests:

            # here we ensure we are looking for a .py file...
            if not selector_path_parts[-1].endswith("py"):
                selector_path_parts = list(selector_path_parts)
                selector_path_parts[-1] = f"{selector_path_parts[-1]}.py"
            selector_path_parts = tuple(selector_path_parts)

            test_parts = _split_test_spec(test)
            num_test_parts = len(test_parts)
            test_path_parts = test_parts[0].parts
            num_test_path_parts = len(test_path_parts)

            paths_equal = False
            if num_selector_path_parts <= num_test_path_parts:
                selector_path = selector_path_parts[-num_selector_path_parts:]
                test_path = test_path_parts[-num_selector_path_parts:]
                paths_equal = selector_path == test_path

            path = str(test_parts[0])
            path_test = str(selector_parts[0])

            if not paths_equal:
                paths_equal = fnmatch(path, path_test)

            test_names_equal = False
            if (num_selector_parts == 2) and (num_test_parts == 2):
                test_names_equal = fnmatch(test_parts[-1], selector_parts[-1])

            if paths_equal and test_names_equal:
                results.append(test)
    return results


def assert_lines_match(
    expected: str, reported: str, squash_spaces: bool = True, ignore_empty=True
):
    """
    compare two multi line strings line by line with stripping and raise an assertion if they don't match
    note: empty lines are ignoresd by default, and multiple spaces are squashed
    Args:
        expected (str): the expected string
        reported (str): the input string
        squash_spaces (bool): remove duplicate spaces before comparison

    Returns:
        None
    """
    lines_expected = expected.split("\n")
    lines_reported = reported.split("\n")

    if ignore_empty:
        lines_expected = [line for line in lines_expected if len(line.strip()) != 0]
        lines_reported = [line for line in lines_reported if len(line.strip()) != 0]

    zip_lines = zip_longest(lines_expected, lines_reported, fillvalue="")
    for i, (expected_line, reported_line) in enumerate(zip_lines):

        expected_line_stripped = expected_line.strip()
        reported_line_stripped = reported_line.strip()

        if squash_spaces:
            expected_line_stripped = " ".join(expected_line_stripped.split())
            reported_line_stripped = " ".join(reported_line_stripped.split())

        if reported_line_stripped != expected_line_stripped:

            for line in lines_expected:
                print(f"exp|{line}")
            print()

            for line in lines_reported:
                print(f"rep|{line}")
            print()

            print("line that caused the error:")
            print()

            print(f"exp|{i}|  |{expected_line_stripped}|")
            print(f"rep|{i}|  |{reported_line_stripped}|")

        assert reported_line_stripped == expected_line_stripped


def isolate_frame(target: str, name: str) -> Optional[str]:
    """
    Extract one frame from a NEF file by name as a string
    Args:
        target (Entry): target NEF entry
        name (str): name of the save frame

    Returns:
        Optional[str]: the entry or a None if not found
    """

    entry = Entry.from_string(target)
    entry = str(entry.get_saveframe_by_name(name))

    return entry


def path_in_parent_directory(root: str, target: str) -> str:
    """
    given a root and a relative path find the relative file path

    Args:
        root (str): root of the path
        target (str): the relative path from the root

    Returns:
        str: the target paths as a string
    """
    parent_path = Path(root).parent
    return str(Path(parent_path, target).absolute())


def root_path(initial_path: str):
    """given a path work up the directory structure till you find the
    directory containing the nef executable

    initial_path (str): the path to start searching from
    """

    target = Path(initial_path)

    belt_and_braces = 100  # noqa: F841 this appears to be a bug
    while (
        not (Path(target.root) == target)
        and not (target / "src" / "nef_pipelines" / "main.py").is_file()
    ):
        target = target.parent
        belt_and_braces -= 1
        if belt_and_braces < 0:
            msg = f"""\
                Error, while search for the rot of the path {initial_path} i walked up 100
                directories this looks like a bug!
            """
            raise Exception(msg)

    return target


# TODO: remove local we now use a hierarchical search
def path_in_test_data(root: str, file_name: str) -> str:
    """
    given a root and a file name find the relative to the file
    in the parents test_data directory

    Args:
        root (str): root of the path
        file_name (str): the name of the file

    Returns:
        str: the target paths as a string
    """

    test_data_local = root_path(root) / "src" / "nef_pipelines" / "tests" / "test_data"
    test_data_root = path_in_parent_directory(root, "test_data")

    if (Path(test_data_local) / file_name).is_file():
        test_data = test_data_local
    else:
        test_data = test_data_root

    # TODO: add an error on shadowing global files

    return str(Path(test_data, file_name).absolute())


def run_and_report(
    typer_app: Typer,
    args: List[str],
    input: IO[AnyStr] = None,
    expected_exit_code: int = 0,
) -> Result:
    """
    run a typer app in the typer test harness and report exceptions and stdout to screen if there is an error
    :param typer_app: the typer app hosting the application
    :param args: command line arguments for the app
    :param input: an input stream if required
    :param expected_exit_code: what exit code to expect if the app is expected to end with an error
    :return: results object
    """

    runner = CliRunner()
    result = runner.invoke(typer_app, args, input=input)

    if result.exit_code != expected_exit_code:
        print("\n", "-" * 40, "-stdout-", "-" * 40)
        print(result.stdout)
        if result.exception:
            print("-" * 40, "exception", "-" * 40)
            formatted = list(traceback.TracebackException(*result.exc_info).format())

            # TODO: this is a hack, I would love to have a better solution!
            if "SystemExit" in formatted[-1]:
                for i, line in enumerate(reversed(formatted)):
                    if (
                        "During handling of the above exception, another exception occurred"
                        in line
                    ):
                        break
                formatted = formatted[: -i - 2]
            print("".join(formatted))

        print("-" * 40, "-" * 9, "-" * 40)

    assert result.exit_code == expected_exit_code

    return result
