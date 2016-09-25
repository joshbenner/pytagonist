# Pytagonist

[![Build Status](https://travis-ci.org/joshbenner/pytagonist.svg?branch=master)](https://travis-ci.org/joshbenner/pytagonist)

Pytagonist is a Python library for parsing API Blueprint documents into
[API Elements](http://api-elements.readthedocs.io/en/latest/)
structures. It is a wrapper around the
[Drafter](https://github.com/apiaryio/drafter) library.

## The Name

Pytagonist is a questionable play on the Node.js wrapper of Drafter,
called [Protagonist](https://github.com/apiaryio/protagonist), which is
itself a cleverly-named cousin to the core C library that does the real
parsing, [Snow Crash](https://github.com/apiaryio/snowcrash).

## Parsing

```python
from pytagonist import parse

with open('/path/to/my_api.apib') as f:
    source = f.read()

ast = parse(source)
```

The resulting data is a API Elements tree.

You can also yield raw JSON or YAML representations of the AST with
calls to `parse_to`.

## Installation

```bash
$ pip install git+https://github.com/joshbenner/pytagonist.git#egg=pytagonist
```
