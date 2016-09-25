import json

from pytagonist import parse_to, FORMAT_JSON, parse, check

simple_apib = """
# Test API

# Group Foo

## Resource Bar [/bar]

### Action Baz [GET]
+ Response 200 (test/plain)

        Hello World!
"""

# Hello world is not indented enough.
simple_apib_with_errors = """
# Test API

# Group Foo

## Resource Bar [/bar]

### Action Baz [GET]
+ Response 200 (test/plain)

    Hello World!
"""


def test_parse_to_simple():
    parsed = parse_to(simple_apib)
    assert isinstance(parsed, basestring)


def test_parse_to_json():
    parsed = json.loads(parse_to(simple_apib, format=FORMAT_JSON))
    assert isinstance(parsed, dict)


def test_parse():
    parsed = parse(simple_apib)
    assert isinstance(parsed, dict)


def test_check():
    result = check(simple_apib)
    assert result is None


def test_check_with_errors():
    result = check(simple_apib_with_errors)
    assert result is not None
