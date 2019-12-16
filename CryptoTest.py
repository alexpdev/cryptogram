from unittest import TestCase
from encrypt import encypher
import string

class CryptoTest(TestCase):

    def setUp(self):
        self.phrase = "MOOSE"
        self.alpha = string.ascii_uppercase

    def test_cypher(self):
        key,phrase = encypher(self.phrase)
        for i in self.alpha:
            self.assertIn(i,key.values())
            self.assertIn(i,key.keys())
            self.assertNotEqual(key[i],i)
        self.assertEqual(len(phrase),len(self.phrase))
