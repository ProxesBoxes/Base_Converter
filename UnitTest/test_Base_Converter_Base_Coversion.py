import unittest

import Base_Converter
import Charsets


class TestBaseConverter(unittest.TestCase):

    def test_2_to_16_1(self):
        base_convert = Base_Converter.BaseConverter(2, ["1010100"], 16)
        base_convert.convert()
        self.assertEqual([["5", "4"]], base_convert.ending_base_values)

    def test_2_to_16_2(self):
        base_convert = Base_Converter.BaseConverter(2, ["1101000"], 16)
        base_convert.convert()
        self.assertEqual([["6", "8"]], base_convert.ending_base_values)

    def test_2_to_16_3(self):
        base_convert = Base_Converter.BaseConverter(2, ["1100101"], 16)
        base_convert.convert()
        self.assertEqual([["6", "5"]], base_convert.ending_base_values)

    def test_2_to_16_multiple(self):
        base_convert = Base_Converter.BaseConverter(2, ["1010100", "1101000", "1100101"], 16)
        base_convert.convert()
        self.assertEqual([["5", "4"], ["6", "8"], ["6", "5"]], base_convert.ending_base_values)

    def test_16_to_10_1(self):
        base_convert = Base_Converter.BaseConverter(16, ["74"], 10)
        base_convert.convert()
        self.assertEqual([["1", "1", "6"]], base_convert.ending_base_values)

    def test_16_to_10_2(self):
        base_convert = Base_Converter.BaseConverter(16, ["69"], 10)
        base_convert.convert()
        self.assertEqual([["1", "0", "5"]], base_convert.ending_base_values)

    def test_16_to_10_3(self):
        base_convert = Base_Converter.BaseConverter(16, ["6D"], 10)
        base_convert.convert()
        self.assertEqual([["1", "0", "9"]], base_convert.ending_base_values)

    def test_16_to_10_4(self):
        base_convert = Base_Converter.BaseConverter(16, ["65"], 10)
        base_convert.convert()
        self.assertEqual([["1", "0", "1"]], base_convert.ending_base_values)

    def test_8_to_32_1(self):
        base_convert = Base_Converter.BaseConverter(8, ["150"], 32)
        base_convert.convert()
        self.assertEqual([["3", "8"]], base_convert.ending_base_values)

    def test_8_to_32_2(self):
        base_convert = Base_Converter.BaseConverter(8, ["141"], 32)
        base_convert.convert()
        self.assertEqual([["3", "1"]], base_convert.ending_base_values)

    def test_8_to_32_3(self):
        base_convert = Base_Converter.BaseConverter(8, ["163"], 32)
        base_convert.convert()
        self.assertEqual([["3", "J"]], base_convert.ending_base_values)

    def test_24_to_23_1(self):
        base_convert = Base_Converter.BaseConverter(24, ["37"], 23)
        base_convert.convert()
        self.assertEqual([["3", "A"]], base_convert.ending_base_values)

    def test_24_to_23_2(self):
        base_convert = Base_Converter.BaseConverter(24, ["4I"], 23)
        base_convert.convert()
        self.assertEqual([["4", "M"]], base_convert.ending_base_values)

    def test_24_to_23_3(self):
        base_convert = Base_Converter.BaseConverter(24, ["44"], 23)
        base_convert.convert()
        self.assertEqual([["4", "8"]], base_convert.ending_base_values)

    def test_24_to_23_4(self):
        base_convert = Base_Converter.BaseConverter(24, ["45"], 23)
        base_convert.convert()
        self.assertEqual([["4", "9"]], base_convert.ending_base_values)

    def test_24_to_23_5(self):
        base_convert = Base_Converter.BaseConverter(24, ["4I"], 23)
        base_convert.convert()
        self.assertEqual([["4", "M"]], base_convert.ending_base_values)

    def test_2_to_3_1(self):
        base_convert = Base_Converter.BaseConverter(2, ["1101111"], 3)
        base_convert.convert()
        self.assertEqual([["1", "1", "0", "1", "0"]], base_convert.ending_base_values)

    def test_2_to_3_2(self):
        base_convert = Base_Converter.BaseConverter(2, ["1100110"], 3)
        base_convert.convert()
        self.assertEqual([["1", "0", "2", "1", "0"]], base_convert.ending_base_values)

    def test_13_to_13_1(self):
        base_convert = Base_Converter.BaseConverter(13, ["81"], 13)
        base_convert.convert()
        self.assertEqual([["8", "1"]], base_convert.ending_base_values)

    def test_7_to_64_1(self):
        base_convert = Base_Converter.BaseConverter(7, ["201"], 64)
        base_convert.convert()
        self.assertEqual([["1", "Z"]], base_convert.ending_base_values)

    def test_7_to_64_2(self):
        base_convert = Base_Converter.BaseConverter(7, ["216"], 64)
        base_convert.convert()
        self.assertEqual([["1", "f"]], base_convert.ending_base_values)

    def test_7_to_64_3(self):
        base_convert = Base_Converter.BaseConverter(7, ["214"], 64)
        base_convert.convert()
        self.assertEqual([["1", "d"]], base_convert.ending_base_values)

    def test_7_to_64_4(self):
        base_convert = Base_Converter.BaseConverter(7, ["203"], 64)
        base_convert.convert()
        self.assertEqual([["1", "\\"]], base_convert.ending_base_values)

    def test_907_to_57_1(self):
        base_convert = Base_Converter.BaseConverter(907, ["U+0061"], 57, Charsets.unicode_charset,
                                                    Charsets.unicode_charset)
        base_convert.convert()
        self.assertEqual([["U", "+", "0", "0", "0", "1", "U", "+", "0", "0", "2", "8"]],
                         base_convert.ending_base_values)

    def test_907_to_57_2(self):
        base_convert = Base_Converter.BaseConverter(907, ["U+0072"], 57, Charsets.unicode_charset,
                                                    Charsets.unicode_charset)
        base_convert.convert()
        self.assertEqual([["U", "+", "0", "0", "0", "2", "U", "+", "0", "0", "0", "0"]], base_convert.ending_base_values)

    def test_907_to_57_3(self):
        base_convert = Base_Converter.BaseConverter(907, ["U+0065"], 57, Charsets.unicode_charset,
                                                    Charsets.unicode_charset)
        base_convert.convert()
        self.assertEqual([["U", "+", "0", "0", "0", "1", "U", "+", "0", "0", "2", "C"]], base_convert.ending_base_values)

    def test_2558_to_70_1(self):
        base_convert = Base_Converter.BaseConverter(2558, ["U+0066"], 70, Charsets.unicode_charset,
                                                    Charsets.unicode_charset)
        base_convert.convert()
        self.assertEqual([["U", "+", "0", "0", "0", "1", "U", "+", "0", "0", "2", "0"]], base_convert.ending_base_values)

    def test_2558_to_70_2(self):
        base_convert = Base_Converter.BaseConverter(2558, ["U+006F"], 70, Charsets.unicode_charset,
                                                    Charsets.unicode_charset)
        base_convert.convert()
        self.assertEqual([["U", "+", "0", "0", "0", "1", "U", "+", "0", "0", "2", "9"]], base_convert.ending_base_values)

    def test_2558_to_70_3(self):
        base_convert = Base_Converter.BaseConverter(2558, ["U+0072"], 70, Charsets.unicode_charset,
                                                    Charsets.unicode_charset)
        base_convert.convert()
        self.assertEqual([["U", "+", "0", "0", "0", "1", "U", "+", "0", "0", "2", "C"]], base_convert.ending_base_values)

    def test_6_to_69_1(self):
        base_convert = Base_Converter.BaseConverter(6, ["155"], 69)
        base_convert.convert()
        self.assertEqual([["1", "2"]], base_convert.ending_base_values)

    def test_6_to_69_2(self):
        base_convert = Base_Converter.BaseConverter(6, ["313"], 69)
        base_convert.convert()
        self.assertEqual([["1", "g"]], base_convert.ending_base_values)

    def test_6_to_69_3(self):
        base_convert = Base_Converter.BaseConverter(6, ["300"], 69)
        base_convert.convert()
        self.assertEqual([["1", "^"]], base_convert.ending_base_values)

    def test_6_to_69_4(self):
        base_convert = Base_Converter.BaseConverter(6, ["303"], 69)
        base_convert.convert()
        self.assertEqual([["1", "a"]], base_convert.ending_base_values)

    def test_112_to_1114111_1(self):
        base_convert = Base_Converter.BaseConverter(118, ["U+0074"], 1114111, Charsets.unicode_charset,
                                                    Charsets.unicode_charset)
        base_convert.convert()
        self.assertEqual([["U", "+", "0", "0", "0", "0", "U", "+", "0", "0", "7", "4"]], base_convert.ending_base_values)

    def test_112_to_1114111_2(self):
        base_convert = Base_Converter.BaseConverter(112, ["U+0068"], 1114111, Charsets.unicode_charset,
                                                    Charsets.unicode_charset)
        base_convert.convert()
        self.assertEqual([["U", "+", "0", "0", "0", "0", "U", "+", "0", "0", "6", "8"]], base_convert.ending_base_values)

    def test_112_to_1114111_3(self):
        base_convert = Base_Converter.BaseConverter(112, ["U+0065"], 1114111, Charsets.unicode_charset,
                                                    Charsets.unicode_charset)
        base_convert.convert()
        self.assertEqual([["U", "+", "0", "0", "0", "0", "U", "+", "0", "0", "6", "5"]], base_convert.ending_base_values)

    def test_10_to_87_1(self):
        base_convert = Base_Converter.BaseConverter(10, ["121"], 87)
        base_convert.convert()
        self.assertEqual([["1", "Y"]], base_convert.ending_base_values)

    def test_10_to_87_2(self):
        base_convert = Base_Converter.BaseConverter(10, ["111"], 87)
        base_convert.convert()
        self.assertEqual([["1", "O"]], base_convert.ending_base_values)

    def test_10_to_87_3(self):
        base_convert = Base_Converter.BaseConverter(10, ["117"], 87)
        base_convert.convert()
        self.assertEqual([["1", "U"]], base_convert.ending_base_values)

    def test_StartingValueNotSet_after_empty_string(self):
        self.assertRaises(Base_Converter.BaseConverterException.StartingValue.NotSet, Base_Converter.BaseConverter(1, "")
                          .convert)


if __name__ == '__main__':
    unittest.main()
