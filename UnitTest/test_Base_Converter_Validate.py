import unittest

import Base_Converter
from Base_Converter_Exceptions import BaseConverterException


class MyTestCase(unittest.TestCase):

    def test_validate_stating_pass(self):
        converter = Base_Converter.BaseConverter(2, 1, 2)
        self.assertTrue(converter.validate())

    def test_validate_stating_raise_starting(self):
        converter = Base_Converter.BaseConverter(0, 1, 2)
        self.assertRaises(BaseConverterException.InvalidBase, converter.validate)

    def test_validate_ending_raise_starting(self):
        converter = Base_Converter.BaseConverter(2, 1, 1)
        self.assertRaises(BaseConverterException.InvalidBase, converter.validate)


if __name__ == '__main__':
    unittest.main()
