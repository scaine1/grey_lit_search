#!/usr/bin/env python
import logging
from logging import StreamHandler, FileHandler
import sys
import click

from grey_lit_search import search_and_download

formatter = logging.Formatter(
    fmt="%(asctime)s: %(levelname)s: %(name)s: %(message)s", datefmt="%Y-%m-%d %H:%M%S"
)

handlers = []
stream_handler = StreamHandler(sys.stdout)
stream_handler.setFormatter(formatter)
handlers.append(stream_handler)

file_handler = FileHandler(filename="googlesearch.log")
file_handler.setFormatter(formatter)
handlers.append(file_handler)

logging.basicConfig(level=logging.INFO, handlers=handlers)

logger = logging.getLogger(__name__)


@click.command()
@click.option("--url", "-u", required=True)
@click.option("--results", "-r", type=int, default=100)
def greysearch(url, results):
    search_and_download(url, results)


if __name__ == "__main__":
    greysearch()
