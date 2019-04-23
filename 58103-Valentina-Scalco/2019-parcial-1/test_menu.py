import unittest
from menu import a

class ErrorFromInput(unittest.TestCase):
    def test_1(self):
        resu = a('Hola')
        self.assertEqual(resu,'ERROR - Ingrese solo numeros')
    def test_3(self):
        resu = a('10')
        self.assertEqual(resu,'10')
if __name__ == "__main__":
    unittest.main()