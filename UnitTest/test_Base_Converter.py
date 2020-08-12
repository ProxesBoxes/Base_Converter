import unittest
import Charsets
import Base_Converter


class TestBaseConverter(unittest.TestCase):

    def test_2_to_16_1(self):
        base_convert = Base_Converter.BaseConverter(2, "1010100", 16)
        base_convert.convert()
        self.assertEqual("54", base_convert.return_output_for_viewing())

    def test_2_to_16_2(self):
        base_convert = Base_Converter.BaseConverter(2, "1101000", 16)
        base_convert.convert()
        self.assertEqual("68", base_convert.return_output_for_viewing())

    def test_2_to_16_3(self):
        base_convert = Base_Converter.BaseConverter(2, "1100101", 16)
        base_convert.convert()
        self.assertEqual("65", "".join(base_convert.ending_base_value))

    def test_16_to_10_1(self):
        base_convert = Base_Converter.BaseConverter(16, "74", 10)
        base_convert.convert()
        self.assertEqual("116", "".join(base_convert.ending_base_value))

    def test_16_to_10_2(self):
        base_convert = Base_Converter.BaseConverter(16, "69", 10)
        base_convert.convert()
        self.assertEqual("105", "".join(base_convert.ending_base_value))

    def test_16_to_10_3(self):
        base_convert = Base_Converter.BaseConverter(16, "6D", 10)
        base_convert.convert()
        self.assertEqual("109", "".join(base_convert.ending_base_value))

    def test_16_to_10_4(self):
        base_convert = Base_Converter.BaseConverter(16, "65", 10)
        base_convert.convert()
        self.assertEqual("101", "".join(base_convert.ending_base_value))

    def test_8_to_32_1(self):
        base_convert = Base_Converter.BaseConverter(8, "150", 32)
        base_convert.convert()
        self.assertEqual("38", "".join(base_convert.ending_base_value))

    def test_8_to_32_2(self):
        base_convert = Base_Converter.BaseConverter(8, "141", 32)
        base_convert.convert()
        self.assertEqual("31", "".join(base_convert.ending_base_value))

    def test_8_to_32_3(self):
        base_convert = Base_Converter.BaseConverter(8, "163", 32)
        base_convert.convert()
        self.assertEqual("3J", "".join(base_convert.ending_base_value))

    def test_24_to_23_1(self):
        base_convert = Base_Converter.BaseConverter(24, "37", 23)
        base_convert.convert()
        self.assertEqual("3A", "".join(base_convert.ending_base_value))

    def test_24_to_23_2(self):
        base_convert = Base_Converter.BaseConverter(24, "4I", 23)
        base_convert.convert()
        self.assertEqual("4M", "".join(base_convert.ending_base_value))

    def test_24_to_23_3(self):
        base_convert = Base_Converter.BaseConverter(24, "44", 23)
        base_convert.convert()
        self.assertEqual("48", "".join(base_convert.ending_base_value))

    def test_24_to_23_4(self):
        base_convert = Base_Converter.BaseConverter(24, "45", 23)
        base_convert.convert()
        self.assertEqual("49", "".join(base_convert.ending_base_value))

    def test_24_to_23_5(self):
        base_convert = Base_Converter.BaseConverter(24, "4I", 23)
        base_convert.convert()
        self.assertEqual("4M", "".join(base_convert.ending_base_value))

    def test_2_to_3_1(self):
        base_convert = Base_Converter.BaseConverter(2, "1101111", 3)
        base_convert.convert()
        self.assertEqual("11010", "".join(base_convert.ending_base_value))

    def test_2_to_3_2(self):
        base_convert = Base_Converter.BaseConverter(2, "1100110", 3)
        base_convert.convert()
        self.assertEqual("10210", "".join(base_convert.ending_base_value))

    def test_13_to_13_1(self):
        base_convert = Base_Converter.BaseConverter(13, "81", 13)
        base_convert.convert()
        self.assertEqual("81", "".join(base_convert.ending_base_value))

    def test_7_to_64_1(self):
        base_convert = Base_Converter.BaseConverter(7, "201", 64)
        base_convert.convert()
        self.assertEqual("1Z", "".join(base_convert.ending_base_value))

    def test_7_to_64_2(self):
        base_convert = Base_Converter.BaseConverter(7, "216", 64)
        base_convert.convert()
        self.assertEqual("1f", "".join(base_convert.ending_base_value))

    def test_7_to_64_3(self):
        base_convert = Base_Converter.BaseConverter(7, "214", 64)
        base_convert.convert()
        self.assertEqual("1d", "".join(base_convert.ending_base_value))

    def test_7_to_64_4(self):
        base_convert = Base_Converter.BaseConverter(7, "203", 64)
        base_convert.convert()
        self.assertEqual("1\\", base_convert.return_output_for_viewing())

    def test_907_to_57_1(self):
        base_convert = Base_Converter.BaseConverter(907, "U+0061", 57, Charsets.unicode_charset,
                                                    Charsets.unicode_charset)
        base_convert.convert()
        self.assertEqual("U+0001 U+0028", base_convert.return_output_for_viewing())

    def test_907_to_57_2(self):
        base_convert = Base_Converter.BaseConverter(907, "U+0072", 57, Charsets.unicode_charset,
                                                    Charsets.unicode_charset)
        base_convert.convert()
        self.assertEqual("U+0002 U+0000", base_convert.return_output_for_viewing())

    def test_907_to_57_3(self):
        base_convert = Base_Converter.BaseConverter(907, "U+0065", 57, Charsets.unicode_charset,
                                                    Charsets.unicode_charset)
        base_convert.convert()
        self.assertEqual("U+0001 U+002C", base_convert.return_output_for_viewing())

    def test_2558_to_70_1(self):
        base_convert = Base_Converter.BaseConverter(2558, "U+0066", 70, Charsets.unicode_charset,
                                                    Charsets.unicode_charset)
        base_convert.convert()
        self.assertEqual("U+0001 U+0020", base_convert.return_output_for_viewing())

    def test_2558_to_70_2(self):
        base_convert = Base_Converter.BaseConverter(2558, "U+006F", 70, Charsets.unicode_charset,
                                                    Charsets.unicode_charset)
        base_convert.convert()
        self.assertEqual("U+0001 U+0029", base_convert.return_output_for_viewing())

    def test_2558_to_70_3(self):
        base_convert = Base_Converter.BaseConverter(2558, "U+0072", 70, Charsets.unicode_charset,
                                                    Charsets.unicode_charset)
        base_convert.convert()
        self.assertEqual("U+0001 U+002C", base_convert.return_output_for_viewing())

    def test_6_to_69_1(self):
        base_convert = Base_Converter.BaseConverter(6, "155", 69)
        base_convert.convert()
        self.assertEqual("12", base_convert.return_output_for_viewing())

    def test_6_to_69_2(self):
        base_convert = Base_Converter.BaseConverter(6, "313", 69)
        base_convert.convert()
        self.assertEqual("1g", base_convert.return_output_for_viewing())

    def test_6_to_69_3(self):
        base_convert = Base_Converter.BaseConverter(6, "300", 69)
        base_convert.convert()
        self.assertEqual("1^", base_convert.return_output_for_viewing())

    def test_6_to_69_4(self):
        base_convert = Base_Converter.BaseConverter(6, "303", 69)
        base_convert.convert()
        self.assertEqual("1a", base_convert.return_output_for_viewing())

    def test_112_to_1114111_1(self):
        base_convert = Base_Converter.BaseConverter(118, "U+0074", 1114111, Charsets.unicode_charset,
                                                    Charsets.unicode_charset)
        base_convert.convert()
        self.assertEqual("U+0000 U+0074", base_convert.return_output_for_viewing())

    def test_112_to_1114111_2(self):
        base_convert = Base_Converter.BaseConverter(112, "U+0068", 1114111, Charsets.unicode_charset,
                                                    Charsets.unicode_charset)
        base_convert.convert()
        self.assertEqual("U+0000 U+0068", base_convert.return_output_for_viewing())

    def test_112_to_1114111_3(self):
        base_convert = Base_Converter.BaseConverter(112, "U+0065", 1114111, Charsets.unicode_charset,
                                                    Charsets.unicode_charset)
        base_convert.convert()
        self.assertEqual("U+0000 U+0065", base_convert.return_output_for_viewing())

    def test_10_to_87_1(self):
        base_convert = Base_Converter.BaseConverter(10, "121", 87)
        base_convert.convert()
        self.assertEqual("1Y", base_convert.return_output_for_viewing())

    def test_10_to_87_2(self):
        base_convert = Base_Converter.BaseConverter(10, "111", 87)
        base_convert.convert()
        self.assertEqual("1O", base_convert.return_output_for_viewing())

    def test_10_to_87_3(self):
        base_convert = Base_Converter.BaseConverter(10, "117", 87)
        base_convert.convert()
        self.assertEqual("1U", base_convert.return_output_for_viewing())


if __name__ == '__main__':
    unittest.main()
