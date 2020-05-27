#!/usr/bin/python
# Author:   @BlankGodd

from setuptools import setup

with open('README.md', 'r') as ld:
    long_description = ld.read()

setup(
    name="blyrics",
    version="0.0.3",
    author="Damilare Agbabiaka (BlankGodd)",
    author_email="blankgodd33@gmail.com",
    description="Python client for the GENIUS API - "
                  "Also for getting latest articles and charts",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/BlankGodd/BLyrics"
    py_modules=["blyrics","interact","save","search","tool","web"],
    package_dir = {"":"blyrics"},
    install_requires=[
        "wget~=3.2",
        "requests~=2.21.0",
        "pyfiglet~=0.8.post1",
        "beautifulsoup4~=4.9.0",
    ],
    classifiers=[
        "Environment :: Console",
        "Intended Audience :: Developers",
        "Natural Language :: English",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Utilities",
        "Topic :: Lyrics",
        "Topic :: Music",
        "Topic :: Internet",
        "Topic :: Multimedia :: Audio",
        "Topic :: Social"
    ],  
    python_requires='>=3.6',
    project_urls={
        "Bug Reports": "https://github.com/BlankGodd/BLyrics/issues",
        "Read the Docs": "https://blyrics.readthedocs.io/en/latest/",
    },
    keywords=["music", "lyrics", "mp3", "music charts", "entertainment",
             "genius", "articles"],
)