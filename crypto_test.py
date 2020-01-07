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



from classes import Phrase

class TestPhrase(unittest.TestCase):

    def setUp(self):
        self.phrase = Phrase.create("THE EYE OF THE TIGER")

    def test_Phrase(self):
        self.assertFalse(self.phrase.swaps)
        self.assertFalse(self.phrase.indeces)
        return

    def test_Phrase_splitter(self):
        lst = self.phrase.splitter()
        self.assertEqual(len(lst),len(self.phrase.split(' ')))
        for i in lst:
            self.assertIsInstance(i,Phrase)
        return

    def test_phrase_mapper(self):
        self.assertEqual(len(self.phrase.mapp),len(self.phrase))


class TestPhraseWithSwaps(unittest.TestCase):

    def setUp(self):
        self.phrase = Phrase.create("FSL LYL OR FSL FIGLP",swaps={"F":"T","L":"E","R":"F","S":"H","P":"R"})

    def test_Phrase(self):
        self.assertTrue(self.phrase.swaps)
        self.assertTrue(self.phrase.indeces)
        return

    def test_Phrase_splitter(self):
        lst = self.phrase.splitter()
        self.assertEqual(len(lst),len(self.phrase.split(' ')))
        for i in lst:
            self.assertIsInstance(i,Phrase)
        return

    def test_phrase_mapper(self):
        self.assertEqual(len(self.phrase.mapp),len(self.phrase))
        print(self.phrase.mapp)
