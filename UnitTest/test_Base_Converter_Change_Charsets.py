import unittest
import Charsets
import Base_Converter


class MyTestCase(unittest.TestCase):

    def test_standard_base2_to_unicode_base2(self):
        base_convert = Base_Converter.BaseConverter(2, "101", 2, Charsets.standard_charset,
                                                    Charsets.unicode_charset)
        base_convert.convert()
        self.assertEqual("U+0001 U+0000 U+0001", base_convert.return_output_for_viewing())

    def test_standard_base2_to_unicode_base16(self):
        base_convert = Base_Converter.BaseConverter(2, "1010100", 16, Charsets.standard_charset,
                                                    Charsets.unicode_charset)
        base_convert.convert()
        self.assertEqual("U+0005 U+0004", base_convert.return_output_for_viewing())

    def test_standard_base10_to_ascii_base256(self):
        base_convert = Base_Converter.BaseConverter(10, "65", 256, Charsets.standard_charset,
                                                    Charsets.ascii_charset)
        base_convert.convert()
        self.assertEqual('\x00A', base_convert.return_output_for_viewing())

    def test_unicode_base16_to_standard_base10(self):
        base_convert = Base_Converter.BaseConverter(16, "U+0001 U+0004", 10, Charsets.unicode_charset,
                                                    Charsets.standard_charset)
        base_convert.convert()
        self.assertEqual("20", base_convert.return_output_for_viewing())

    def test_unicode_base256_to_ascii_base256(self):
        base_convert = Base_Converter.BaseConverter(256, "U+0041", 256, Charsets.unicode_charset,
                                                    Charsets.ascii_charset)
        base_convert.convert()
        self.assertEqual('\x00A', base_convert.return_output_for_viewing())

    def test_ascii_base_256_to_standard_base10(self):
        base_convert = Base_Converter.BaseConverter(256, "A", 10, Charsets.ascii_charset,
                                                    Charsets.standard_charset)
        base_convert.convert()
        self.assertEqual("65", base_convert.return_output_for_viewing())

    def test_ascii_base_256_to_unicode_base800(self):
        base_convert = Base_Converter.BaseConverter(256, "A", 800, Charsets.ascii_charset,
                                                    Charsets.unicode_charset)
        base_convert.convert()
        self.assertEqual("U+0000 U+0041", base_convert.return_output_for_viewing())


if __name__ == '__main__':
    unittest.main()
