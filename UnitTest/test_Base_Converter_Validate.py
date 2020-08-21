import unittest

import Base_Converter
from Base_Converter_Exceptions import BaseConverterException


class MyTestCase(unittest.TestCase):

    def test_validate_stating_pass(self):
        self.assertTrue(Base_Converter.BaseConverter(2, ["1"], 2).validate())

    def test_validate_stating_raise_starting(self):
        self.assertRaises(BaseConverterException.InvalidBase, Base_Converter.BaseConverter(0, ["1"], 2).validate)

    def test_validate_ending_raise_starting(self):
        self.assertRaises(BaseConverterException.InvalidBase, Base_Converter.BaseConverter(2, ["1"], 1).validate)

    def test_validate_no_starting_base_values(self):
        self.assertRaises(BaseConverterException.StartingValue.NotSet, Base_Converter.BaseConverter(1).validate)

    def test_validate_no_starting_base_not_list_of_strings(self):
        self.assertRaises(BaseConverterException.StartingValue.NotSet, Base_Converter.BaseConverter(1, []).validate)


if __name__ == '__main__':
    unittest.main()
