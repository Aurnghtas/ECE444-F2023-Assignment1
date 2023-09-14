import unittest
from utils import Utils

class testMyUtils(unittest.TestCase):
    def test_reversed_string(self):
        utils = Utils()
        with self.assertRaises(ValueError):
            utils.reversed("123")

    def test_reversed_floats(self):
        utils = Utils()
        with self.assertRaises(ValueError):
            utils.reversed(123.321)

    def test_reversed_integer(self):
        utils = Utils()
        self.assertEqual(utils.reversed(123), 321)

    def test_formatter_string(self):
        utils = Utils()
        with self.assertRaises(ValueError):
            utils.formatter("123")

    def test_formatter_floats(self):
        utils = Utils()
        with self.assertRaises(ValueError):
            utils.formatter(123.321)

    def test_formatter_integer(self):
        utils = Utils()
        self.assertEqual(utils.formatter(123), (bin(123), oct(123)))


if __name__ == '__main__':
    unittest.main()