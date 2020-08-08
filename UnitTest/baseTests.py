import unittest
import Base_Converter


class MyTestCase(unittest.TestCase):
    my_converter = Base_Converter.converter()

    def tearDown(self):
        self.my_converter.ending_base_value = ""

    def set_bases(self, starting, ending):

        self.my_converter.starting_base = starting
        self.my_converter.starting_base_chars = Base_Converter.get_charset(self.my_converter.starting_base)
        self.my_converter.ending_base = ending
        if self.my_converter.starting_base < 254:
            self.my_converter.ending_base_chars = Base_Converter.get_charset(self.my_converter.ending_base)
        else:
            self.my_converter.ending_base_chars = Base_Converter.generate_unicodes(self.my_converter.ending_base)

    def test_2_to_16_1(self):
        self.set_bases(2, 16)
        self.my_converter.starting_base_value = Base_Converter.split("1010100")
        self.my_converter.convert()
        self.assertEqual("54", "".join(self.my_converter.ending_base_value))

    def test_2_to_16_2(self):
        self.set_bases(2, 16)
        self.my_converter.starting_base_value = Base_Converter.split("1101000")
        self.my_converter.convert()
        self.assertEqual("68", "".join(self.my_converter.ending_base_value))

    def test_2_to_16_3(self):
        self.set_bases(2, 16)
        self.my_converter.starting_base_value = Base_Converter.split("1100101")
        self.my_converter.convert()
        self.assertEqual("65", "".join(self.my_converter.ending_base_value))

    def test_16_to_10_1(self):
        self.set_bases(16, 10)
        self.my_converter.starting_base_value = Base_Converter.split("74")
        self.my_converter.convert()
        self.assertEqual("116", "".join(self.my_converter.ending_base_value))

    def test_16_to_10_2(self):
        self.set_bases(16, 10)
        self.my_converter.starting_base_value = Base_Converter.split("69")
        self.my_converter.convert()
        self.assertEqual("105", "".join(self.my_converter.ending_base_value))

    def test_16_to_10_3(self):
        self.set_bases(16, 10)
        self.my_converter.starting_base_value = Base_Converter.split("6D")
        self.my_converter.convert()
        self.assertEqual("109", "".join(self.my_converter.ending_base_value))

    def test_16_to_10_4(self):
        self.set_bases(16, 10)
        self.my_converter.starting_base_value = Base_Converter.split("65")
        self.my_converter.convert()
        self.assertEqual("101", "".join(self.my_converter.ending_base_value))

    def test_8_to_32_1(self):
        self.set_bases(8, 32)
        self.my_converter.starting_base_value = Base_Converter.split("150")
        self.my_converter.convert()
        self.assertEqual("38", "".join(self.my_converter.ending_base_value))

    def test_8_to_32_2(self):
        self.set_bases(8, 32)
        self.my_converter.starting_base_value = Base_Converter.split("141")
        self.my_converter.convert()
        self.assertEqual("31", "".join(self.my_converter.ending_base_value))

    def test_8_to_32_3(self):
        self.set_bases(8, 32)
        self.my_converter.starting_base_value = Base_Converter.split("163")
        self.my_converter.convert()
        self.assertEqual("3J", "".join(self.my_converter.ending_base_value))

    def test_24_to_23_1(self):
        self.set_bases(24, 23)
        self.my_converter.starting_base_value = Base_Converter.split("37")
        self.my_converter.convert()
        self.assertEqual("3A", "".join(self.my_converter.ending_base_value))
    def test_24_to_23_2(self):
        self.set_bases(24, 23)
        self.my_converter.starting_base_value = Base_Converter.split("4I")
        self.my_converter.convert()
        self.assertEqual("4M", "".join(self.my_converter.ending_base_value))
    def test_24_to_23_3(self):
        self.set_bases(24, 23)
        self.my_converter.starting_base_value = Base_Converter.split("44")
        self.my_converter.convert()
        self.assertEqual("48", "".join(self.my_converter.ending_base_value))
    def test_24_to_23_4(self):
        self.set_bases(24, 23)
        self.my_converter.starting_base_value = Base_Converter.split("45")
        self.my_converter.convert()
        self.assertEqual("49", "".join(self.my_converter.ending_base_value))
    def test_24_to_23_5(self):
        self.set_bases(24, 23)
        self.my_converter.starting_base_value = Base_Converter.split("4I")
        self.my_converter.convert()
        self.assertEqual("4M", "".join(self.my_converter.ending_base_value))

    def test_2_to_3_1(self):
        self.set_bases(2, 3)
        self.my_converter.starting_base_value = Base_Converter.split("1101111")
        self.my_converter.convert()
        self.assertEqual("11010", "".join(self.my_converter.ending_base_value))

    def test_2_to_3_2(self):
        self.set_bases(2, 3)
        self.my_converter.starting_base_value = Base_Converter.split("1100110")
        self.my_converter.convert()
        self.assertEqual("10210", "".join(self.my_converter.ending_base_value))

    def test_13_to_13_1(self):
        self.set_bases(13, 13)
        self.my_converter.starting_base_value = Base_Converter.split("81")
        self.my_converter.convert()
        self.assertEqual("81", "".join(self.my_converter.ending_base_value))

    def test_7_to_64_1(self):
        self.set_bases(7, 64)
        self.my_converter.starting_base_value = Base_Converter.split("201")
        self.my_converter.convert()
        self.assertEqual("1Z", "".join(self.my_converter.ending_base_value))

    def test_7_to_64_2(self):
        self.set_bases(7, 64)
        self.my_converter.starting_base_value = Base_Converter.split("216")
        self.my_converter.convert()
        self.assertEqual("1f", "".join(self.my_converter.ending_base_value))

    def test_7_to_64_3(self):
        self.set_bases(7, 64)
        self.my_converter.starting_base_value = Base_Converter.split("214")
        self.my_converter.convert()
        self.assertEqual("1d", "".join(self.my_converter.ending_base_value))

    def test_7_to_64_4(self):
        self.set_bases(7, 64)
        self.my_converter.starting_base_value = Base_Converter.split("203")
        self.my_converter.convert()
        self.assertEqual("1\\", "".join(self.my_converter.ending_base_value))

    def test_907_to_57_1(self):
        self.set_bases(907, 57)
        self.my_converter.starting_base_value = "U+0061"
        self.my_converter.convert()
        self.assertEqual("U+0001U+0028", "".join(self.my_converter.ending_base_value))

    def test_907_to_57_2(self):
        self.set_bases(907, 57)
        self.my_converter.starting_base_value = "U+0072"
        self.my_converter.convert()
        self.assertEqual("U+0002U+0000", "".join(self.my_converter.ending_base_value))

    def test_907_to_57_3(self):
        self.set_bases(907, 57)
        self.my_converter.starting_base_value = "U+0065"
        self.my_converter.convert()
        self.assertEqual("U+0001U+002C", "".join(self.my_converter.ending_base_value))

    def test_2558_to_70_1(self):
        self.set_bases(2558, 70)
        self.my_converter.starting_base_value = "U+0066"
        self.my_converter.convert()
        self.assertEqual("U+0001U+0020", "".join(self.my_converter.ending_base_value))

    def test_2558_to_70_2(self):
        self.set_bases(2558, 70)
        self.my_converter.starting_base_value = "U+006F"
        self.my_converter.convert()
        self.assertEqual("U+0001U+0029", "".join(self.my_converter.ending_base_value))

    def test_2558_to_70_3(self):
        self.set_bases(2558, 70)
        self.my_converter.starting_base_value = "U+0072"
        self.my_converter.convert()
        self.assertEqual("U+0001U+002C", "".join(self.my_converter.ending_base_value))

    def test_6_to_69_1(self):
        self.set_bases(6, 69)
        self.my_converter.starting_base_value = Base_Converter.split("155")
        self.my_converter.convert()
        self.assertEqual("12", "".join(self.my_converter.ending_base_value))

    def test_6_to_69_2(self):
        self.set_bases(6, 69)
        self.my_converter.starting_base_value = Base_Converter.split("313")
        self.my_converter.convert()
        self.assertEqual("1g", "".join(self.my_converter.ending_base_value))

    def test_6_to_69_3(self):
        self.set_bases(6, 69)
        self.my_converter.starting_base_value = Base_Converter.split("300")
        self.my_converter.convert()
        self.assertEqual("1^", "".join(self.my_converter.ending_base_value))

    def test_6_to_69_4(self):
        self.set_bases(6, 69)
        self.my_converter.starting_base_value = Base_Converter.split("303")
        self.my_converter.convert()
        self.assertEqual("1a", "".join(self.my_converter.ending_base_value))

    def test_112_to_1114111_1(self):
        self.set_bases(112, 1114111)
        self.my_converter.starting_base_value = "U+0074"
        self.my_converter.convert()
        self.assertEqual("U+0000U+0074", "".join(self.my_converter.ending_base_value))

    def test_112_to_1114111_1(self):
        self.set_bases(112, 1114111)
        self.my_converter.starting_base_value = "U+0068"
        self.my_converter.convert()
        self.assertEqual("U+0000U+0068", "".join(self.my_converter.ending_base_value))

    def test_112_to_1114111_1(self):
        self.set_bases(112, 1114111)
        self.my_converter.starting_base_value = "U+0065"
        self.my_converter.convert()
        self.assertEqual("U+0000U+0065", "".join(self.my_converter.ending_base_value))

    def test_10_to_87_1(self):
        self.set_bases(10, 87)
        self.my_converter.starting_base_value = Base_Converter.split("121")
        self.my_converter.convert()
        self.assertEqual("1Y", "".join(self.my_converter.ending_base_value))

    def test_10_to_87_2(self):
        self.set_bases(10, 87)
        self.my_converter.starting_base_value = Base_Converter.split("111")
        self.my_converter.convert()
        self.assertEqual("1O", "".join(self.my_converter.ending_base_value))

    def test_10_to_87_3(self):
        self.set_bases(10, 87)
        self.my_converter.starting_base_value = Base_Converter.split("117")
        self.my_converter.convert()
        self.assertEqual("1U", "".join(self.my_converter.ending_base_value))



if __name__ == '__main__':
    unittest.main()
