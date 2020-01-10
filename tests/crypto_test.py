from utils import uniques
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

from PhraseClass import Phrase

class TestPhrase(TestCase):

    def setUp(self):
        self.phrase = Phrase.create("THE EYE OF THE TIGER")

    def test_Phrase(self):
        self.assertFalse(self.phrase.key)
        return

class TestPhraseWithSwaps(TestCase):

    def setUp(self):
        self.phrase = Phrase.create("FSL LYL OR FSL FIGLP",{"F":"T","L":"E","R":"F","S":"H","P":"R"})

    def test_Phrase(self):
        self.assertTrue(self.phrase.key)
        self.assertTrue(self.phrase.amount)
        return

class TestUtils(TestCase):

    def setUp(self):
        self.string = "HELLO"

    def uniques(self):
        a = uniques(self.string)
        self.assertEqual(len(a),4)
