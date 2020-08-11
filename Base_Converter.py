import string
import math
import re

# All bases start with

normal_ascii_max_size = 256

standard_base_10 = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]

unicode_start = "U+"
unicode_format = unicode_start + "{:04X}"
unicode_format_width = 6

standard_charset = "standard"
ascii_charset = "ascii"
unicode_charset = "unicode"
charset = [standard_charset, unicode_charset, ascii_charset]


def split(word):
    return [char for char in word]


def generate_unicode_set(base):
    unicode_values = []
    for i in range(base):
        unicode_values += [unicode_format.format(i)]
    return unicode_values


def generate_normal_ascii_set(base):
    if abs(base) > normal_ascii_max_size:
        raise Exception("Base exceeds " + str(normal_ascii_max_size) + " thus \"normal_ascii_set\" can not be used.")
    return generate_ascii_set(base)


def generate_ascii_set(base, offset=0):
    if (abs(base) + offset) > normal_ascii_max_size:
        raise Exception("Base exceeds standard ascii set please use a custom defined set")

    asci_values = []
    for i in range(base):
        asci_values += [chr(i + offset)]
    return asci_values


def generate_standard_base_set(base):
    standard_base_set = standard_base_10
    if base <= 10:
        return standard_base_set[:base]

    return standard_base_set + generate_ascii_set(base - 10, 65)


class BaseConverter:

    def __init__(self, input_base, input_value, output_base, input_set=standard_charset, output_set=None):
        if output_set is None:
            output_set = input_set

        self.starting_base = input_base
        self.starting_base_chars = input_set
        self.starting_base_value = input_value
        self.starting_base_charset = input_set

        if self.starting_base_charset == standard_charset:
            self.starting_base_chars = generate_standard_base_set(self.starting_base)
        elif self.starting_base_charset == unicode_charset:
            self.starting_base_chars = generate_unicode_set(self.starting_base)
        elif self.starting_base_charset == ascii_charset:
            self.starting_base_chars = generate_ascii_set(self.starting_base)

        self.ending_base = output_base
        self.ending_base_chars = output_set
        self.ending_base_charset = output_set

        if self.ending_base_charset == standard_charset:
            self.ending_base_chars = generate_standard_base_set(self.ending_base)
        elif self.ending_base_charset == unicode_charset:
            self.ending_base_chars = generate_unicode_set(self.ending_base)
        elif self.ending_base_charset == ascii_charset:
            self.ending_base_chars = generate_ascii_set(self.ending_base)

        self.ending_base_value = []

        self.starting_base_value.strip()

        if input_set == standard_charset:
            self.starting_base_value = split(input_value)
        elif input_set == unicode_charset:
            self.starting_base_value = re.split(unicode_format, input_value)
        elif input_set == ascii_charset:
            self.starting_base_value = split(input_value)

    def convert(self):
        # start with converting to base 10 value so we can maths
        position = 0
        base_10_value = 0

        self.starting_base_value.reverse()

        for char in self.starting_base_value:
            i = self.starting_base_chars.index(char)
            base_10_value += i * (math.pow(self.starting_base, position))
            position += 1

        self.recuse_convert(base_10_value)

    def recuse_convert(self, value):
        cur_pos = math.floor(value / self.ending_base)
        if cur_pos >= self.ending_base:
            self.recuse_convert(cur_pos)
        else:
            self.ending_base_value += self.ending_base_chars[cur_pos]
        mod_val = value % self.ending_base
        self.ending_base_value += self.ending_base_chars[math.floor(mod_val)]

    def return_output_for_viewing(self):
        output = "".join(self.ending_base_value)

        if self.ending_base_charset == unicode_charset:
            output = ' '.join([output[i:i + unicode_format_width] for i in range(0, len(output), unicode_format_width)])
            "".join(self.ending_base_value)

        return output
