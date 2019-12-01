'''Pip setup script.'''
from setuptools import setup

from grey_lit_search import __version__

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name='grey_lit_search',
    version=__version__,
    author='Simon Caine',
    author_email='sclives@gmail.com',
    description="program to download pdf files from google search",
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=['grey_lit_search'],
    package_dir={'grey_lit_search': 'grey_lit_search'},
    zip_safe=False,
    classifiers=[
        'Programming Language :: Python :: 3'
    ],
    python_requires='>=3.6',
    install_requires=['beautifulsoup4', 'requests', 'click'],
    entry_points={'console_scripts': ['greysearch = grey_lit_search.greysearch: greysearch']},
    )
