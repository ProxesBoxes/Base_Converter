import string
import math
import re

# All bases start with

standard_base_10 = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
standard_ascii = list(string.ascii_uppercase) + ["[", "\\", "]", "^", "_", "`"] + list(string.ascii_lowercase) + \
    ["{", "|", "}", "~", "DEL", "Ç", "ü", "é", "â", "ä", "à", "å", "ç", "ê", "ë", "è", "ï", "î", "ì", ""]

unicode_format = "U+{:04X}"
unicode_format_width = 6


def split(word):
    return [char for char in word]


def generate_unicode_set(base):
    unicode_values = []
    for i in range(base):
        unicode_values += [unicode_format.format(i)]
    return unicode_values


def get_charset(base):
    ''' False denotes custom base was provided '''

    if base <= 10:
        return standard_base_10[:base]
    elif base <= 87:
        return standard_base_10 + standard_ascii[:base - 10]

    return generate_unicode_set(base)


class BaseConverter:

    def __init__(self, input_base, input_value, output_base):
        self.starting_base = 0
        self.starting_base_chars = []
        self.starting_base_value = []
        self.ending_base = 0
        self.ending_base_chars = []
        self.ending_base_value = []

        self.starting_base = input_base
        self.starting_base_chars = get_charset(self.starting_base)

        # Logic for breaking any input of base not using the "unicode" values by character otherwise break by
        # "character set"
        input_value.strip()
        if self.starting_base < len(standard_ascii):
            self.starting_base_value = split(input_value)
        else:
            # TODO: need to valid this works as expected
            self.starting_base_value = re.split(unicode_format, input_value)

        self.ending_base = output_base

        if self.starting_base < len(standard_ascii):
            self.ending_base_chars = get_charset(self.ending_base)
        else:
            self.ending_base_chars = generate_unicode_set(self.ending_base)

    def convert(self):
        # start with converting to base 10 value so we can maths
        position = 0
        base_10_value = 0
        if self.starting_base_value[:2] != "U+":
            self.starting_base_value.reverse()

            for char in self.starting_base_value:
                i = self.starting_base_chars.index(char)
                base_10_value += i * (math.pow(self.starting_base, position))
                position += 1
        else:
            base_10_value += self.starting_base_chars.index(self.starting_base_value)
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
        output = 0
        output = "".join(self.ending_base_value)
        if (self.starting_base >= len(standard_ascii)) or (self.ending_base >= len(standard_ascii)):
            output = ' '.join([output[i:i+unicode_format_width] for i in range(0, len(output), unicode_format_width)])
            "".join(self.ending_base_value)

        return output
