import unittest
import Base_Converter
import Charsets


class MyTestCase(unittest.TestCase):

    def setUp(self):
        self.converter = Base_Converter.BaseConverter(0, 0, 0)

    def tearDown(self):
        self.converter = None

    def test_54_to_base10_standard(self):
        self.converter.ending_base = 10
        self.converter.ending_base_chars = Charsets.generate_standard_set(10)
        self.converter.recuse_convert(54)
        self.assertEqual(["5", "4"], self.converter.ending_base_value)

    def test_54_to_base100_unicode(self):
        self.converter.ending_base = 100
        self.converter.ending_base_chars = Charsets.generate_unicode_set(100)
        self.converter.recuse_convert(54)
        self.assertEqual(["U", "+", "0", "0", "0", "0", "U", "+", "0", "0", "3", "6"], self.converter.ending_base_value)

    def test_54_to_base100_ascii(self):
        self.converter.ending_base = 256
        self.converter.ending_base_chars = Charsets.generate_ascii_set(100)
        self.converter.recuse_convert(65)
        self.assertEqual(["\x00", "A"], self.converter.ending_base_value)


if __name__ == '__main__':
    unittest.main()
