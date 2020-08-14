import re

import Globals
from Base_Converter_Exceptions import BaseConverterException

standard_base_10 = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]

unicode_start = "U+"
unicode_format = unicode_start + "{:04X}"
unicode_format_width = 6

standard_charset = "standard"
ascii_charset = "ascii"
unicode_charset = "unicode"
predefined_charsets = [standard_charset, unicode_charset, ascii_charset]


def generate_standard_set(base):
    standard_base_set = standard_base_10
    # TODO: abs needed for negative values
    if base <= 10:
        return standard_base_set[:base]

    return standard_base_set + generate_ascii_set(base - 10, 65)


def generate_unicode_set(base):
    unicode_values = []

    # TODO: use abs of base for negative values
    for i in range(base):
        unicode_values += [unicode_format.format(i)]
    return unicode_values


def generate_normal_ascii_set(base):
    if abs(base) > Globals.normal_ascii_max_size:
        raise BaseConverterException.BaseExceedsSet.NormalAscii
    return generate_ascii_set(base)


def generate_ascii_set(base, offset=0):
    if (abs(base) + offset) > Globals.normal_ascii_max_size:
        raise BaseConverterException.BaseExceedsSet.Standard

    asci_values = []
    for i in range(base):
        asci_values += [chr(i + offset)]
    return asci_values


def get_chars(base, charset):
    if standard_charset == charset:
        return generate_standard_set(base)
    elif unicode_charset == charset:
        return generate_unicode_set(base)
    elif ascii_charset == charset:
        return generate_ascii_set(base)

    return charset


def detect_charset(value):
    # A simplistic way of attempting to determine the character set

    if re.search("^U\\+[0-9A-F]{4}", value):
        return unicode_charset

    if re.search("[\\x00-\\x2F\\x3A-\\x40\\x7B-\\x7F-\\xFF]+", value):
        return ascii_charset

    return standard_charset
