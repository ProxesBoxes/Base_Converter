import unittest
import Base_Converter
import string


class BasicConvertStaticFunctions(unittest.TestCase):

    def test_split(self):
        self.assertEqual(["1", "2", "3"], Base_Converter.split("123"))

    def test_generate_unicode_set(self):
        expected = [Base_Converter.unicode_start + "0000", Base_Converter.unicode_start + "0001",
                    Base_Converter.unicode_start + "0002", Base_Converter.unicode_start + "0003",
                    Base_Converter.unicode_start + "0004", Base_Converter.unicode_start + "0005",
                    Base_Converter.unicode_start + "0006", Base_Converter.unicode_start + "0007",
                    Base_Converter.unicode_start + "0008", Base_Converter.unicode_start + "0009",
                    Base_Converter.unicode_start + "000A", Base_Converter.unicode_start + "000B",
                    Base_Converter.unicode_start + "000C", Base_Converter.unicode_start + "000D",
                    Base_Converter.unicode_start + "000E", Base_Converter.unicode_start + "000F",
                    Base_Converter.unicode_start + "0010", Base_Converter.unicode_start + "0011"]
        output = Base_Converter.generate_unicode_set(18)
        self.assertEqual(expected, output)

    def test_generate_standard_base_set(self):
        expected = Base_Converter.standard_base_10 + Base_Converter.split(string.ascii_uppercase) + \
                   Base_Converter.split("[\\]^_`") + Base_Converter.split(string.ascii_lowercase)
        output = Base_Converter.generate_standard_base_set(len(expected))
        self.assertEqual(expected, output)

    def test_generate_standard_base_10set(self):
        expected = Base_Converter.standard_base_10
        output = Base_Converter.generate_standard_base_set(10)
        self.assertEqual(expected, output)

    def test_generate_normal_ascii_set(self):
        expected = [chr(0), chr(1), chr(2), chr(3), chr(4), chr(5), chr(6), chr(7), chr(8), chr(9), chr(10), chr(11)]
        output = Base_Converter.generate_normal_ascii_set(12)
        self.assertEqual(expected, output)

    def test_generate_normal_ascii_set_expect_exception(self):
        self.assertRaises(Exception, Base_Converter.generate_normal_ascii_set, Base_Converter.normal_ascii_max_size+10)

    def test_generate_ascii_offset_set(self):
        expected = [chr(20), chr(21), chr(22), chr(23), chr(24), chr(25), chr(26), chr(27), chr(28), chr(29), chr(30)]
        output = Base_Converter.generate_ascii_set(11, 20)
        self.assertEqual(expected, output)

    def test_generate_normal_ascii_set_expect_exception(self):
        self.assertRaises(Exception, Base_Converter.generate_ascii_set, Base_Converter.normal_ascii_max_size, 1)


if __name__ == '__main__':
    unittest.main()
