#!/usr/bin/python
# Author:   @BlankGodd

from setuptools import setup

with open('description.rst', 'r') as fh:
    long_description = fh.read()

setup(
    name="blyrics",
    version="1.1",
    author="Damilare Agbabiaka (BlankGodd)",
    author_email="blankgodd33@gmail.com",
    description="Python client for the GENIUS API -     Also for getting latest articles and charts",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/BlankGodd/BLyrics",
    py_modules=["blyrics","interact","save","search","tool","web"],
    package_dir = {"":"blyrics"},
    install_requires=[
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
        "Topic :: Artistic Software",
        "Topic :: Games/Entertainment",
        "Topic :: Internet",
        "Topic :: Internet :: WWW/HTTP :: Dynamic Content :: Content Management System",
        "Topic :: Internet :: WWW/HTTP :: Indexing/Search",
        "Topic :: Multimedia :: Sound/Audio"
    ],  
    python_requires='>=3.6',
    project_urls={
        "Bug Reports": "https://github.com/BlankGodd/BLyrics/issues",
        "Read the Docs": "https://github.com/BlankGodd/BLyrics/wiki",
    },
    keywords=["music", "lyrics", "mp3", "music charts", "entertainment",
             "genius", "articles"],
)