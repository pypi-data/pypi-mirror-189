import sys
from argparse import Namespace
from contextlib import contextmanager
from io import StringIO

import pytest

# from pandas import DataFrame
from pynmrstar import Entry, Loop

from nef_pipelines.lib.nef_lib import (  # dataframe_to_loop,; loop_to_dataframe,; NEF_CATEGORY_ATTR,
    create_entry_from_stdin_or_exit,
    loop_row_dict_iter,
    loop_row_namespace_iter,
    select_frames_by_name,
)
from nef_pipelines.lib.test_lib import assert_lines_match, path_in_test_data

# def test_nef_to_pandas():
#
#     TEST_DATA_NEF = """
#         loop_
#           _test_loop.tag_1 _test_loop.tag_2
#           1                 2
#           3                 .
#         stop_
#     """
#
#     loop = Loop.from_string(TEST_DATA_NEF, convert_data_types=True)
#     result = loop_to_dataframe(loop)
#
#     EXPECTED_DATA_FRAME = DataFrame()
#     EXPECTED_DATA_FRAME["tag_1"] = ["1", "3"]
#     EXPECTED_DATA_FRAME["tag_2"] = ["2", "."]
#
#     assert result.equals(EXPECTED_DATA_FRAME)
#
#
# def test_pandas_to_nef():
#
#     TEST_DATA_NEF = """
#         loop_
#           _test_loop.tag_1 _test_loop.tag_2
#           1                 2
#           3                 .
#         stop_
#     """
#
#     EXPECTED_NEF = Loop.from_string(TEST_DATA_NEF)
#
#     data_frame = DataFrame()
#     data_frame["tag_1"] = ["1", "3"]
#     data_frame["tag_2"] = ["2", "."]
#
#     result = dataframe_to_loop(data_frame, category="test_loop")
#
#     assert result == EXPECTED_NEF


# def test_nef_category():
#
#     TEST_DATA_NEF = """
#         loop_
#           _test_loop.tag_1 _test_loop.tag_2
#           1                 2
#           3                 .
#         stop_
#     """
#
#     loop = Loop.from_string(TEST_DATA_NEF, convert_data_types=True)
#     frame = loop_to_dataframe(loop)
#
#     assert frame.attrs[NEF_CATEGORY_ATTR] == "test_loop"
#
#     new_loop = dataframe_to_loop(frame)
#
#     # note pynmrstar includes the leading _ in the category, I don't...!
#     assert new_loop.category == "_test_loop"
#
#     new_loop_2 = dataframe_to_loop(frame, category="wibble")
#     # note pynmrstar includes the leading _ in the category, I don't...!
#     assert new_loop_2.category == "_wibble"


def test_select_frames():
    TEST_DATA = """\
    data_test
        save_test_frame_1
            _test.sf_category test
            loop_
                _test.col_1
                .
            stop_
        save_


        save_test_frame_2
            _test.sf_category test
            loop_
                _test.col_1
                .
            stop_
        save_

        save_test_frame_13
            _test.sf_category test
            loop_
                _test.col_1
                .
            stop_
        save_

    """

    test = Entry.from_string(TEST_DATA)

    frames = select_frames_by_name(test, "test_frame_1")

    assert len(frames) == 1
    assert frames[0].name == "test_frame_1"

    frames = select_frames_by_name(test, ["test_frame_13"])

    assert len(frames) == 1
    assert frames[0].name == "test_frame_13"

    frames = select_frames_by_name(test, "frame_")
    assert len(frames) == 3
    names = sorted([frame.name for frame in frames])
    assert names == ["test_frame_1", "test_frame_13", "test_frame_2"]

    frames = select_frames_by_name(test, ["frame_1"], exact=False)

    assert len(frames) == 2
    names = sorted([frame.name for frame in frames])
    assert names == ["test_frame_1", "test_frame_13"]

    frames = select_frames_by_name(test, ["*frame_1*"])

    assert len(frames) == 2
    names = sorted([frame.name for frame in frames])
    assert names == ["test_frame_1", "test_frame_13"]

    frames = select_frames_by_name(test, ["frame_[1]"])

    assert len(frames) == 2
    names = sorted([frame.name for frame in frames])
    assert names == ["test_frame_1", "test_frame_13"]

    frames = select_frames_by_name(test, ["frame_[2]"])

    assert len(frames) == 1
    assert frames[0].name == "test_frame_2"


@contextmanager
def replace_stdin(target: str):
    """The provided input should be the text the user inputs. It support multiple lines for multiple inputs"""
    orig = sys.stdin
    sys.stdin = StringIO(target)
    yield
    sys.stdin = orig


def test_read_entry_stdin_or_exit_empty_stdin(clear_cache):
    with replace_stdin(""):
        with pytest.raises(SystemExit) as pytest_wrapped_e:
            create_entry_from_stdin_or_exit()

    assert pytest_wrapped_e.type == SystemExit
    assert pytest_wrapped_e.value.code == 1


@pytest.mark.skip(reason="not currently working and deprecated")
def test_read_entry_stdin_or_exit(clear_cache):

    EXPECTED = """\
    data_new

    save_nef_nmr_meta_data
       _nef_nmr_meta_data.sf_category      nef_nmr_meta_data
       _nef_nmr_meta_data.sf_framecode     nef_nmr_meta_data
       _nef_nmr_meta_data.format_name      nmr_exchange_format
       _nef_nmr_meta_data.format_version   1.1
       _nef_nmr_meta_data.program_name     NEFPipelines
       _nef_nmr_meta_data.program_version  0.0.1
       _nef_nmr_meta_data.script_name      header.py
       _nef_nmr_meta_data.creation_date    2021-06-19T21:13:32.548158
       _nef_nmr_meta_data.uuid             NEFPipelines-2021-06-19T21:13:32.548158-0485797022

       loop_
          _nef_run_history.run_number
          _nef_run_history.program_name
          _nef_run_history.program_version
          _nef_run_history.script_name
          _nef_run_history.uuid

          1 NEFPipelines 1.1 header.py NEFPipelines-2021-06-19T21:13:32.548158-0485797022

       stop_

    save_

    """
    path = path_in_test_data(__file__, "header.nef")
    lines = open(path).read()

    with replace_stdin(lines):
        entry = create_entry_from_stdin_or_exit()

    assert_lines_match(str(entry), EXPECTED)


def test_loop_row_dict_iter():
    TEST_DATA = """\
        loop_
            _test.col_1
            _test.col_2
            _test.col_3

            a 2 4.5
            b 3 5.6

        stop_

    """

    loop = Loop.from_string(TEST_DATA)

    EXPECTED = [
        {"col_1": "a", "col_2": 2, "col_3": 4.5},
        {"col_1": "b", "col_2": 3, "col_3": 5.6},
    ]

    result = [row for row in loop_row_dict_iter(loop)]

    assert result == EXPECTED


def test_loop_row_dict_iter_no_convert():
    TEST_DATA = """\
        loop_
            _test.col_1
            _test.col_2
            _test.col_3

            a 2 4.5
            b 3 5.6

        stop_

    """

    loop = Loop.from_string(TEST_DATA)

    EXPECTED = [
        {"col_1": "a", "col_2": "2", "col_3": "4.5"},
        {"col_1": "b", "col_2": "3", "col_3": "5.6"},
    ]

    result = [row for row in loop_row_dict_iter(loop, convert=False)]

    assert result == EXPECTED


def test_loop_row_namespace_iter():
    TEST_DATA = """\
        loop_
            _test.col_1
            _test.col_2
            _test.col_3

            a 2 4.5
            b 3 5.6

        stop_

    """

    loop = Loop.from_string(TEST_DATA)

    EXPECTED = [
        Namespace(col_1="a", col_2=2, col_3=4.5),
        Namespace(col_1="b", col_2=3, col_3=5.6),
    ]

    result = [row for row in loop_row_namespace_iter(loop)]

    assert result == EXPECTED


def test_loop_row_namespace_iter_no_convert():
    TEST_DATA = """\
        loop_
            _test.col_1
            _test.col_2
            _test.col_3

            a 2 4.5
            b 3 5.6

        stop_

    """

    loop = Loop.from_string(TEST_DATA)

    EXPECTED = [
        Namespace(col_1="a", col_2="2", col_3="4.5"),
        Namespace(col_1="b", col_2="3", col_3="5.6"),
    ]

    result = [row for row in loop_row_namespace_iter(loop, convert=False)]

    assert result == EXPECTED
