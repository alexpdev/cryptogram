import unittest
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
