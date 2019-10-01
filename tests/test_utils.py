from pathlib import Path
import os
import shutil

import mock
import pytest
import requests
from requests.exceptions import HTTPError
import grey_lit_search.utils as utl
from grey_lit_search.google import get_search_results

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


def test_get_webpage_with_results(setup):
    url = "https://www.google.com/search?q=sample+pdf"
    webpage = utl.get_webpage(url, results=2, base_dir="tests/test_output")
    assert len(list(get_search_results(webpage))) == 2

    webpage = utl.get_webpage(url, results=100, base_dir="tests/test_output")
    # annoyingly the People also ask and related count when near 100 searchs
    assert len(list(get_search_results(webpage))) >= 98


def test_save_google_search(setup):
    url = "http://fakesite.com/fake_url/"
    webpage_text = "fake webpage content"
    utl.save_google_search(url, webpage_text, base_dir="tests/test_output")
    expected_search_file = "tests/test_output/google-search-term.txt"
    assert os.path.isfile(expected_search_file)

    with open(expected_search_file, "r") as fid:
        expected_term = fid.readline()
    assert expected_term == url

    expected_content_file = "tests/test_output/google-search-result.html"
    assert os.path.isfile(expected_content_file)

    with open(expected_content_file, "r") as fid:
        expected_content = fid.readlines()
    assert expected_content == [webpage_text]


@mock.patch("grey_lit_search.utils.requests.get")
def test_results_summary(mock_requests, setup):
    mock_requests().raise_for_status.return_value = None
    mock_requests().content = b"fake byte data"
    utl.save_pdf(0, "http://fakesite.com/fake0.pdf", base_dir="tests/test_output/")
    utl.save_link(1, "http://fakesite.com/fake_url1/", base_dir="tests/test_output")
    utl.save_pdf(2, "http://fakesite.com/fake2.pdf", base_dir="tests/test_output/")
    utl.save_link(3, "http://fakesite.com/fake_url3/", base_dir="tests/test_output")
    utl.save_pdf(4, "http://fakesite.com/fake4.pdf", base_dir="tests/test_output/")
    utl.save_link(5, "http://fakesite.com/fake_url5/", base_dir="tests/test_output")
    utl.save_link(6, "http://fakesite.com/fake_url6/", base_dir="tests/test_output")
    utl.save_pdf(7, "http://fakesite.com/fake7.pdf", base_dir="tests/test_output/")
    utl.save_pdf(8, "http://fakesite.com/fake8.pdf", base_dir="tests/test_output/")

    expected_summary = "tests/test_output/results_summary.txt"
    assert os.path.isfile(expected_summary)
    with open(expected_summary, "r") as fid:
        summary = fid.readlines()
    assert summary == [
        "000: fake0.pdf\n",
        "001: http://fakesite.com/fake_url1/\n",
        "002: fake2.pdf\n",
        "003: http://fakesite.com/fake_url3/\n",
        "004: fake4.pdf\n",
        "005: http://fakesite.com/fake_url5/\n",
        "006: http://fakesite.com/fake_url6/\n",
        "007: fake7.pdf\n",
        "008: fake8.pdf\n",
    ]


def test_warns_cant_have_more_than_100_results(setup):
    url = "https://www.google.com/search?q=sample+pdf"

    with pytest.warns(utl.SearchWarning) as warnings:
        webpage = utl.get_webpage(url, results=101, base_dir="tests/test_output")
