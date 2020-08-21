import unittest
import Base_Converter
import Charsets


class MyTestCase(unittest.TestCase):

    def setUp(self):
        self.converter = Base_Converter.BaseConverter(0, 0, 0)

    def tearDown(self):
        self.converter = None

    def test_output_value65_standard(self):
        self.converter.ending_base_values = ["6", "5"]
        self.assertEqual("65", self.converter.return_output_for_viewing())

    def test_output_value5_standard(self):
        self.converter.ending_base_values = ["5"]
        self.assertEqual("5", self.converter.return_output_for_viewing())

    def test_output_valueU0000U0065_unicode(self):
        self.converter.ending_base_values = ["U", "+", "0", "0", "0", "0", "U", "+", "0", "0", "6", "5"]
        self.converter.ending_base_charset = Charsets.unicode_charset
        self.assertEqual("U+0000 U+0065", self.converter.return_output_for_viewing())


if __name__ == '__main__':
    unittest.main()
