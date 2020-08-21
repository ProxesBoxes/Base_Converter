import math

import Charsets
import Globals
import Validate
from Base_Converter_Exceptions import BaseConverterException


class BaseConverter:

    def __init__(self, input_base, input_value=None, output_base=None, input_set=Charsets.standard_charset,
                 output_set=None):

        if output_set is None:
            output_set = input_set

        if output_base is None:
            output_base = input_base

        self.starting_base = input_base
        self.starting_base_chars = input_set
        self.starting_base_values = input_value
        self.starting_base_charset = input_set
        self.ending_base = output_base
        self.ending_base_chars = output_set
        self.ending_base_charset = output_set
        self.ending_base_values = []

    def set_input_value(self, input_blob, value_delimiter=" "):
        self.starting_base_values = input_blob.split(value_delimiter)

    def convert(self):
        self.validate()
        self.populate_chars()
        # start with converting to base 10 value so we can maths
        for starting_base_value in self.starting_base_values:
            self.ending_base_values.append(self.recuse_convert(self.get_base10_value(starting_base_value)))

    def validate(self):
        if not self.starting_base_values:
            raise BaseConverterException.StartingValue.NotSet()

        if not Validate.is_list_of_strings(self.starting_base_values):
            raise BaseConverterException.StartingValue.NotListOfStrings()

        # TODO: use abs when validating for negative bases
        if self.starting_base < 2:
            raise BaseConverterException.InvalidBase("starting")

        if self.ending_base < 2:
            raise BaseConverterException.InvalidBase("ending")

        return True

    def populate_chars(self):
        self.starting_base_chars = Charsets.get_chars(self.starting_base, self.starting_base_charset)
        self.ending_base_chars = Charsets.get_chars(self.ending_base, self.ending_base_charset)

    def get_base10_value(self, starting_base_value):

        # quick logic to exit out if starting base is 10 and is the standard charset
        if self.starting_base == 10 and self.starting_base_charset == Charsets.standard_charset:
            try:
                return int(starting_base_value)
            except ValueError as error:
                raise BaseConverterException.ExceedsBase.Characters(starting_base_value, self.starting_base,
                                                                    self.starting_base_charset) from error

        starting_value = Globals.split(starting_base_value)
        if self.starting_base_charset == Charsets.unicode_charset:
            starting_value = starting_base_value.split()

        starting_value.reverse()

        position = 0
        base_10_value = 0
        index = 0
        for char in starting_value:
            try:
                index = self.starting_base_chars.index(char)
            except ValueError as error:
                raise BaseConverterException.ExceedsBase.Characters(starting_base_value, self.starting_base,
                                                                    self.starting_base_charset) from error
            base_10_value += index * (math.pow(self.starting_base, position))
            position += 1

        return base_10_value

    def recuse_convert(self, value, ending_base_value=None):
        # Assumes that the value provided is in base 10

        if ending_base_value is None:
            ending_base_value = []

        cur_pos = math.floor(value / self.ending_base)
        if cur_pos >= self.ending_base:
            self.recuse_convert(cur_pos, ending_base_value)
        else:
            try:
                ending_base_value += self.ending_base_chars[cur_pos]
            except IndexError as error:
                raise BaseConverterException.ExceedsBase.Position(cur_pos, self.ending_base, self.ending_base_charset) \
                    from error

        mod_val = value % self.ending_base

        try:
            ending_base_value += self.ending_base_chars[math.floor(mod_val)]
        except IndexError as error:
            raise BaseConverterException.ExceedsBase.Position(math.floor(mod_val), self.ending_base,
                                                              self.ending_base_charset) from error
        return ending_base_value

    def return_output_for_viewing(self):
        output = "".join(self.ending_base_values)

        if self.ending_base_charset == Charsets.unicode_charset:
            output = ' '.join([output[i:i + Charsets.unicode_format_width] for i in range(0, len(output),
                                                                                          Charsets.unicode_format_width)
                               ])
            "".join(self.ending_base_values)

        return output
