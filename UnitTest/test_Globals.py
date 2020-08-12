import unittest
import Globals


class MyTestCase(unittest.TestCase):

    def test_split(self):
        self.assertEqual(["1", "2", "3"], Globals.split("123"))


if __name__ == '__main__':
    unittest.main()
