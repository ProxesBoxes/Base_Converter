import string
import math
import sys

# All bases start with

standard_base_10 = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
standard_ascii = list(string.ascii_uppercase) + ["[", "\\", "]", "^", "_", "`"] + list(string.ascii_lowercase) + \
    ["{", "|", "}", "~", "DEL", "Ç", "ü", "é", "â", "ä", "à", "å", "ç", "ê", "ë", "è", "ï", "î", "ì", ""]


def split(word):
    return [char for char in word]


def generate_unicode_set(base):
    unicode_values = []
    for i in range(base):
        unicode_values += ["U+" + "{:04X}".format(i)]
    return unicode_values


def get_charset(base):
    ''' False denotes custom base was provided '''

    if base <= 10:
        return standard_base_10[:base]
    elif base <= 87:
        return standard_base_10 + standard_ascii[:base - 10]

    return generate_unicode_set(base)


class BaseConverter:
    starting_base = 0
    starting_base_chars = []
    starting_base_value = []
    ending_base = 0
    ending_base_chars = []
    ending_base_value = []

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