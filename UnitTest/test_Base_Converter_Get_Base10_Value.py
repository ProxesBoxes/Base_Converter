import unittest

import Base_Converter
from Base_Converter_Exceptions import BaseConverterException
import Charsets


class MyTestCase(unittest.TestCase):

    def setUp(self):
        self.converter = Base_Converter.BaseConverter(0, 0, 0)

    def tearDown(self):
        self.converter = None

    def test_base10_to_base10_standard(self):
        self.converter.starting_base = 10
        self.converter.starting_base_value = "15"
        self.assertEqual(15, self.converter.get_base10_value())

    def test_base10_to_base10_unicode(self):
        self.converter.starting_base = 10
        self.converter.starting_base_value = "U+0001 U+0005"
        self.converter.starting_base_charset = Charsets.unicode_charset
        self.converter.starting_base_chars = Charsets.generate_unicode_set(10)
        self.assertEqual(15, self.converter.get_base10_value())

    def test_base13_to_base10_standard(self):
        self.converter.starting_base = 13
        self.converter.starting_base_value = "15"
        self.converter.starting_base_chars = Charsets.generate_standard_set(13)
        self.assertEqual(18, self.converter.get_base10_value())

    def test_base5_to_base10_standard(self):
        self.converter.starting_base = 5
        self.converter.starting_base_value = "4"
        self.converter.starting_base_chars = Charsets.generate_standard_set(13)
        self.assertEqual(4, self.converter.get_base10_value())

    def test_base10_exceed_base(self):
        self.converter.starting_base = 10
        self.converter.starting_base_value = "FF"
        self.assertRaises(BaseConverterException.ExceedsBase.Characters, self.converter.get_base10_value)

    def test_base16_exceed_base(self):
        self.converter.starting_base = 16
        self.converter.starting_base_value = "QQ"
        self.converter.starting_base_charset = Charsets.standard_charset
        self.converter.starting_base_chars = Charsets.generate_standard_set(16)
        self.assertRaises(BaseConverterException.ExceedsBase.Characters, self.converter.get_base10_value)


if __name__ == '__main__':
    unittest.main()
