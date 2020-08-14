import string
import unittest

import Charsets
import Globals
from Base_Converter_Exceptions import BaseConverterException


class BasicConvertStaticFunctions(unittest.TestCase):

    def test_generate_unicode_set(self):
        expected = [Charsets.unicode_start + "0000", Charsets.unicode_start + "0001",
                    Charsets.unicode_start + "0002", Charsets.unicode_start + "0003",
                    Charsets.unicode_start + "0004", Charsets.unicode_start + "0005",
                    Charsets.unicode_start + "0006", Charsets.unicode_start + "0007",
                    Charsets.unicode_start + "0008", Charsets.unicode_start + "0009",
                    Charsets.unicode_start + "000A", Charsets.unicode_start + "000B",
                    Charsets.unicode_start + "000C", Charsets.unicode_start + "000D",
                    Charsets.unicode_start + "000E", Charsets.unicode_start + "000F",
                    Charsets.unicode_start + "0010", Charsets.unicode_start + "0011"]
        output = Charsets.generate_unicode_set(18)
        self.assertEqual(expected, output)

    def test_generate_standard_base_set(self):
        expected = Charsets.standard_base_10 + Globals.split(string.ascii_uppercase) + \
                   Globals.split("[\\]^_`") + Globals.split(string.ascii_lowercase)
        output = Charsets.generate_standard_set(len(expected))
        self.assertEqual(expected, output)

    def test_generate_standard_base_10set(self):
        expected = Charsets.standard_base_10
        output = Charsets.generate_standard_set(10)
        self.assertEqual(expected, output)

    def test_generate_normal_ascii_set(self):
        expected = [chr(0), chr(1), chr(2), chr(3), chr(4), chr(5), chr(6), chr(7), chr(8), chr(9), chr(10), chr(11)]
        output = Charsets.generate_normal_ascii_set(12)
        self.assertEqual(expected, output)

    def test_generate_normal_ascii_set_expect_exception(self):
        self.assertRaises(BaseConverterException.BaseExceedsSet.NormalAscii,
                          Charsets.generate_normal_ascii_set, Globals.normal_ascii_max_size+10)

    def test_generate_ascii_offset_set(self):
        expected = [chr(20), chr(21), chr(22), chr(23), chr(24), chr(25), chr(26), chr(27), chr(28), chr(29), chr(30)]
        output = Charsets.generate_ascii_set(11, 20)
        self.assertEqual(expected, output)

    def test_generate_ascii_set_expect_exception(self):
        self.assertRaises(BaseConverterException.BaseExceedsSet.Standard, Charsets.generate_ascii_set,
                          Globals.normal_ascii_max_size, 1)

    def test_get_chars_10_standard(self):
        self.assertEqual(Charsets.generate_standard_set(10),
                         Charsets.get_chars(10, Charsets.standard_charset))

    def test_get_chars_10_unicode(self):
        self.assertEqual(Charsets.generate_unicode_set(10),
                         Charsets.get_chars(10, Charsets.unicode_charset))

    def test_get_chars_10_ascii(self):
        self.assertEqual(Charsets.generate_ascii_set(10),
                         Charsets.get_chars(10, Charsets.ascii_charset))


if __name__ == '__main__':
    unittest.main()
