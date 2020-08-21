import unittest

import Validate


class TestValidate(unittest.TestCase):
    def test_is_list_of_strings_true(self):
        self.assertTrue(Validate.is_list_of_strings([""]))

    def test_is_list_of_strings_false_not_list(self):
        self.assertFalse(Validate.is_list_of_strings(""))

    def test_is_list_of_strings_false_list_empty(self):
        self.assertFalse(Validate.is_list_of_strings([]))

    def test_is_list_of_strings_false_list_numbers(self):
        self.assertFalse(Validate.is_list_of_strings([1, 2, 3]))

    def test_is_list_of_strings_false_list_mixed(self):
        self.assertFalse(Validate.is_list_of_strings([1, "2", 3]))


if __name__ == '__main__':
    unittest.main()
