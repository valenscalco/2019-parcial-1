import unittest
from decimal_hexadecimal import conver

class TestDecimalAHexadecimal(unittest.TestCase):
    def test_decimahex (self):
        result = conver (5)
        self.assertEqual(result, '5')
    def test_decimahex2 (self):
        result = conver (10)
        self.assertEqual(result, 'A')
    def test_decimahex3 (self):
        result = conver (17)
        self.assertEqual(result, '11')
    def test_decimahex4 (self):
        result = conver (1234)
        self.assertEqual(result, '4D2')
if __name__ == '__main__':
   unittest.main()
