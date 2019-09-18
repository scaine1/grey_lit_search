import pytest
from pathlib import Path
from bs4 import BeautifulSoup as soup

from grey_lit_search.google import GoogleResult, get_search_results

test_dir = Path(__file__).resolve().parent.joinpath("test_data")


@pytest.fixture()
def load_sample_result():
    with open(test_dir.joinpath("sample_result.html"), "r") as fid:
        webpage_data = fid.readline()
    return soup(webpage_data, "html.parser").find("div", {"class": "g"})


@pytest.fixture()
def load_sample_result_with_query():
    with open(test_dir.joinpath("sample_result_with_query_string.html"), "r") as fid:
        webpage_data = fid.readline()
    return soup(webpage_data, "html.parser").find("div", {"class": "g"})


@pytest.fixture()
def load_sample_search():
    with open(test_dir.joinpath("sample_search.html"), "r") as fid:
        return "".join(fid.readlines())


def test_google_result_title(load_sample_result):
    result = GoogleResult(load_sample_result)
    assert result.title == "A Simple PDF File"


def test_google_result_links(load_sample_result):
    result = GoogleResult(load_sample_result)
    assert len(result.get_links()) == 4


def test_google_result_primary_link(load_sample_result):
    result = GoogleResult(load_sample_result)
    assert result.primary_link == "http://www.africau.edu/images/default/sample.pdf"


def test_google_result_primary_link_remove_query_string(load_sample_result_with_query):
    result = GoogleResult(load_sample_result_with_query)
    assert result.primary_link == "http://www.africau.edu/images/default/sample.pdf"


def test_get_number_of_individual_search_results(load_sample_search):
    search_generator = get_search_results(load_sample_search)
    assert len(list(search_generator)) == 11


def test_individual_search_results(load_sample_search):
    search_generator = get_search_results(load_sample_search)
    titles = [result.title for result in search_generator]
    expected_titles = [
        "A Simple PDF File",
        "PDF document - pdf 995",
        "Dummy PDF file",
        "PDF Bookmark Sample - Adobe",
        "Sample .pdf download | File Examples Download",
        "Sample PDF Document",
        "This is a test PDF file - UNEC",
        "Prince - Sample Documents - Prince XML",
        "PDF Bean Inc. - PDF Samples- Convert Word, Excel, PowerPoint to ...",
        "PDF Test Page",
        None,
    ]
    assert titles == expected_titles
