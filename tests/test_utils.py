from pathlib import Path
import os
import shutil

import mock
import pytest
import requests
from requests.exceptions import HTTPError
import grey_lit_search.utils as utl

test_dir = Path(__file__).resolve().parent.joinpath("test_data")


@pytest.fixture
def setup():
    # setup
    yield
    # teardown
    if os.path.isdir("tests/test_output"):
        shutil.rmtree("tests/test_output")


def test_write_timeout_message_file_is_created(setup):
    fname = "tests/test_output/pdfs/000/fake.pdf"
    link = "https:fakesite.com/fake.pdf"
    utl.write_timeout_msg(fname, link)
    assert os.path.isfile(f"{fname}.timedout.txt")


def test_write_timeout_message_msg_is_correct(setup):
    fname = "tests/test_output/pdfs/000/fake.pdf"
    link = "https:fakesite.com/fake.pdf"
    utl.write_timeout_msg(fname, link)
    with open(f"{fname}.timedout.txt", "r") as fid:
        lines = fid.readlines()
    assert lines[0] == (
        "timed out when trying to download,"
        " please manually download using the link below\n"
    )
    assert lines[1] == link


def test_write_fail_message_file_is_created(setup):
    fname = "tests/test_output/pdfs/000/fail.pdf"
    link = "https:failsite.com/fail.pdf"
    utl.write_fail_msg(fname, link)
    assert os.path.isfile(f"{fname}.404error.txt")


def test_write_fail_message_msg_is_correct(setup):
    fname = "tests/test_output/pdfs/000/fail.pdf"
    link = "https:failsite.com/fail.pdf"
    utl.write_fail_msg(fname, link)
    with open(f"{fname}.404error.txt", "r") as fid:
        lines = fid.readlines()
    assert lines[0] == ("recieved 404 error when trying to download\n")
    assert lines[1] == link


@mock.patch("grey_lit_search.utils.requests.get")
def test_save_pdf_saves_pdf(mock_requests, setup):
    # mock_requests().status_code.return_value = 200
    mock_requests().raise_for_status.return_value = None
    mock_requests().content = b"fake byte data"
    link = "http://fakesite.com/fake.pdf"
    utl.save_pdf(0, link, base_dir="tests/test_output/pdfs")
    expected_file = "tests/test_output/pdfs/000/fake.pdf"
    assert os.path.isfile(expected_file)
    with open(expected_file, "rb") as fid:
        assert fid.readline() == b"fake byte data"


@mock.patch("grey_lit_search.utils.requests.get")
def test_save_pdf_captures_httperror(mock_requests, setup):
    mock_resp = requests.models.Response()
    mock_resp.status_code = 404
    mock_requests.return_value = mock_resp
    link = "http://fakesite.com/fake.pdf"
    utl.save_pdf(0, link, base_dir="tests/test_output/pdfs")
    expected_file = "tests/test_output/pdfs/000/fake.pdf.404error.txt"
    assert os.path.isfile(expected_file)
    with open(expected_file, "r") as fid:
        lines = fid.readlines()
    assert lines[0] == ("recieved 404 error when trying to download\n")
    assert lines[1] == link


@mock.patch("grey_lit_search.utils.requests.get")
def test_save_pdf_captures_timeouterror(mock_requests, setup):
    mock_requests.side_effect = requests.exceptions.Timeout
    link = "http://fakesite.com/fake.pdf"
    utl.save_pdf(0, link, base_dir="tests/test_output/pdfs")
    expected_file = "tests/test_output/pdfs/000/fake.pdf.timedout.txt"
    assert os.path.isfile(expected_file)
    with open(expected_file, "r") as fid:
        lines = fid.readlines()
    assert lines[0] == (
        "timed out when trying to download,"
        " please manually download using the link below\n"
    )
    assert lines[1] == link


def test_save_link(setup):
    search_num = 4
    link = "http://fakesite.com/fake_url/"
    utl.save_link(search_num, link, base_dir="tests/test_output")
    expected_file = "tests/test_output/004/website_link.txt"
    assert os.path.isfile(expected_file)
    with open(expected_file, "r") as fid:
        saved_link = fid.readline()
    assert saved_link == link
