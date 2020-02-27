from unittest import TestCase
from cryptogram.encrypt import encypher
from cryptogram.decrypt import sanatize
import string

class EncypherTest(TestCase):

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

class DecryptTest(TestCase):

    def setUp(self):
        self.samples = {
            "ME" : "ME",
            "James was Ugly!" : "James was Ugly",
            "I'll" : "I'll",
            "*******" : "",
            "!()^&&$:':;-_a" : "'a",
        }

    def test_sanatize(self):
        for k,v in self.samples.items():
            result = sanatize(k)
            print(result,v)
            self.assertEqual(result,v)
