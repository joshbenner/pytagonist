import json

from _drafter import ffi, lib as drafter


FORMAT_YAML = drafter.DRAFTER_SERIALIZE_YAML
FORMAT_JSON = drafter.DRAFTER_SERIALIZE_JSON


class ParseError(Exception):
    pass


def parse_to(source, format=FORMAT_YAML, sourcemap=False):
    """
    Parse API Blueprint into a target format

    :param source: API Blueprint source
    :type source: str

    :param format: Target format (FORMAT_YAML or FORMAT_JSON)
    :type format: int

    :param sourcemap: Whether to include source map data in result
    :type sourcemap: bool

    :return: String containing AST as YAML or JSON
    :rtype: str
    """
    result = ffi.new('char **')
    options = (sourcemap, format)
    success = drafter.drafter_parse_blueprint_to(source, result, options)
    if success != 0:
        raise ParseError('Unable to parse API Blueprint source code')
    return ffi.string(result[0])


def parse(source, sourcemap=False):
    """
    Parse API Blueprint into Python data

    :param source: API Blueprint source
    :type source: str

    :param sourcemap: Whether to include source map data in result
    :type sourcemap: bool

    :return: API Elements data
    :rtype: dict
    """
    return json.loads(parse_to(source, format=FORMAT_JSON, sourcemap=sourcemap))


def check(source):
    """
    Check API Blueprint syntax

    :param source: API Blueprint source
    :type source: str

    :return: Parsing result, or None if there were no errors.
    :rtype: dict|None
    """
    result = drafter.drafter_check_blueprint(source)

    options = (True, FORMAT_JSON)
    serialized = drafter.drafter_serialize(result, options)

    out = None
    if serialized != ffi.NULL:
        out = json.loads(ffi.string(serialized))

    return out
