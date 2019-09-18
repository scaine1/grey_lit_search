import os
import logging

import requests

"""
Copyright 2019 Simon Caine

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""

logger = logging.getLogger(__name__)


headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36"
}


def save_pdf(search_num, link, base_dir="output", timeout=60):
    """
    given a pdf link download the pdf into a subfolder
    based on the search number
    """

    save_dir = os.path.join(base_dir, f"{str(search_num).zfill(3)}")
    os.makedirs(save_dir, exist_ok=True)
    fname = os.path.join(save_dir, os.path.basename(link))
    logger.info(f"attempting to download {fname}")

    try:
        page = requests.get(link, headers=headers, timeout=60)
        page.raise_for_status()
        with open(fname, "wb") as fid:
            fid.write(page.content)
        logger.info(f"    {fname} saved")
    except requests.exceptions.HTTPError:
        logger.error(f"posted link does not exit")
        write_fail_msg(fname, link)
    except requests.exceptions.Timeout as e:
        logger.warning(f"download failed with error {e}")
        write_timeout_msg(fname, link)


def write_timeout_msg(fname, link):
    """
    Create a file in liew of the correct one that lets the user
    know the request timed out and include link so they can manually
    download the file.

    This can happen if the pdf file is quite large or the internet
    connection is a bit dodgy
    """

    os.makedirs(os.path.dirname(fname), exist_ok=True)

    with open(fname + ".timedout.txt", "w") as fid:
        msg = (
            "timed out when trying to download,"
            " please manually download using the link below\n"
            f"{link}"
        )
        fid.writelines(msg)


def write_fail_msg(fname, link):
    """
    Create a file in liew of the correct one that lets the user
    know the requested link does not exist
    """

    os.makedirs(os.path.dirname(fname), exist_ok=True)

    with open(fname + ".404error.txt", "w") as fid:
        msg = "recieved 404 error when trying to download\n" f"{link}"
        fid.writelines(msg)


def save_link(search_num, link, base_dir="output"):
    """
    given a link that we are not going to download, save the
    link to a text file so the user knows what the link was
    """

    save_dir = os.path.join(base_dir, f"{str(search_num).zfill(3)}")
    os.makedirs(save_dir, exist_ok=True)
    fname = os.path.join(save_dir, "website_link.txt")
    logger.info(f"saving link to {fname}")

    with open(fname, "w") as fid:
        fid.writelines(link)


def get_webpage(url):
    webpage = requests.get(url, headers=headers)
    return webpage.text


def save_google_search(url, webpage_text, base_dir="output"):
    os.makedirs(base_dir, exist_ok=True)
    fname = os.path.join(base_dir, "google-search-term.txt")
    with open(fname, "w") as fid:
        fid.write(url)

    fname = os.path.join(base_dir, "google-search-result.html")
    with open(fname, "w") as fid:
        fid.write(webpage_text)
