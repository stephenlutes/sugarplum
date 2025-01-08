# sugarplum

[![PyPI - Version](https://img.shields.io/pypi/v/sugarplum.svg)](https://pypi.org/project/sugarplum)
[![PyPI - Python Version](https://img.shields.io/pypi/pyversions/sugarplum.svg)](https://pypi.org/project/sugarplum)

-----

Sugarplum is a library for managing inputs (both regular and test inputs) for Advent of Code puzzles.


## Why sugarplum

The creators of Advent of Code have asked that inputs not be shared, including test
inputs (see the links below). However, it can be helpful to not have to download
the puzzle inputs each time switching computers, or to have the test inputs stored for
running unit tests. That is where sugarplum comes in. It allows you to have a seperate 
directory, most likely a private repo, where these are stored, but easily retrieve them
for use in puzzle solutions and tests.

https://www.reddit.com/r/adventofcode/wiki/faqs/copyright/inputs/

https://www.reddit.com/r/adventofcode/comments/zh2hk0/comment/iznly9w/?context=3

## Installation

```console
pip install sugarplum
```

## Usage

The environment variable "SUGARPLUM_BASE_PATH" must be set to the base path of the 
directory where the inputs reside. At the moment, sugarplum is opinionated, expecting a
specific file structure and file names. It expects the directory structure to be one of
YYYY/DD.