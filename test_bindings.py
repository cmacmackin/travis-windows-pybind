import unittest

import CPPMATH

class SimpleTestCase(unittest.TestCase):
    def test_add(self):
        i = 10
        j = 5
        self.assertEqual(i+j, CPPMATH.add(i, j))
