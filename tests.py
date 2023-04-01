from main import *

import unittest
class Maintets(unittest.TestCase):
    def test_division(self):
        self.assertEqual(a(4, 2),2)


    def test_value(self):
        self.assertRaises(TypeError, main , "a", 2)