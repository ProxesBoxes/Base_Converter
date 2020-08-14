import math

import Charsets
import Globals
from Base_Converter_Exceptions import BaseConverterException


class BaseConverter:

    def __init__(self, input_base, input_value, output_base, input_set=Charsets.standard_charset, output_set=None):
        if output_set is None:
            output_set = input_set

        self.starting_base = input_base
        self.starting_base_chars = input_set
        self.starting_base_value = input_value
        self.starting_base_charset = input_set
        self.ending_base = output_base
        self.ending_base_chars = output_set
        self.ending_base_charset = output_set
        self.ending_base_value = []

    def convert(self):
        self.validate()
        self.populate_chars()
        # start with converting to base 10 value so we can maths
        self.recuse_convert(self.get_base10_value())

    def validate(self):
        # TODO: use abs when validating for negative bases
        if self.starting_base < 2:
            raise BaseConverterException.InvalidBase("starting")

        if self.ending_base < 2:
            raise BaseConverterException.InvalidBase("ending")

        return True

    def populate_chars(self):
        self.starting_base_chars = Charsets.get_chars(self.starting_base, self.starting_base_charset)
        self.ending_base_chars = Charsets.get_chars(self.ending_base, self.ending_base_charset)

    def get_base10_value(self):

        # quick logic to exit out if starting base is 10 and is the standard charset
        if self.starting_base == 10 and self.starting_base_charset == Charsets.standard_charset:
            try:
                return int(self.starting_base_value)
            except ValueError as error:
                raise BaseConverterException.ExceedsBase.Characters(self.starting_base_value, self.starting_base,
                                                                    self.starting_base_charset) from error

        starting_value = Globals.split(self.starting_base_value)
        if self.starting_base_charset == Charsets.unicode_charset:
            starting_value = self.starting_base_value.split()

        starting_value.reverse()

        position = 0
        base_10_value = 0
        index = 0
        for char in starting_value:
            try:
                index = self.starting_base_chars.index(char)
            except ValueError as error:
                raise BaseConverterException.ExceedsBase.Characters(self.starting_base_value, self.starting_base,
                                                                    self.starting_base_charset) from error
            base_10_value += index * (math.pow(self.starting_base, position))
            position += 1

        return base_10_value

    def recuse_convert(self, value):
        # Assumes that the value provided is in base 10

        cur_pos = math.floor(value / self.ending_base)
        if cur_pos >= self.ending_base:
            self.recuse_convert(cur_pos)
        else:
            try:
                self.ending_base_value += self.ending_base_chars[cur_pos]
            except IndexError as error:
                raise BaseConverterException.ExceedsBase.Position(cur_pos, self.ending_base, self.ending_base_charset) \
                    from error

        mod_val = value % self.ending_base

        try:
            self.ending_base_value += self.ending_base_chars[math.floor(mod_val)]
        except IndexError as error:
            raise BaseConverterException.ExceedsBase.Position(math.floor(mod_val), self.ending_base,
                                                              self.ending_base_charset) from error

    def return_output_for_viewing(self):
        output = "".join(self.ending_base_value)

        if self.ending_base_charset == Charsets.unicode_charset:
            output = ' '.join([output[i:i + Charsets.unicode_format_width] for i in range(0, len(output),
                                                                                          Charsets.unicode_format_width)
                               ])
            "".join(self.ending_base_value)

        return output
