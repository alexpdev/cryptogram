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

    def test_phrase_map_split(self):
        p1 = Phrase.create("PMMSE DMWN",swaps={"P":"G","M":"O"})
        p2 = Phrase.create("GOOSE DOWN")
        self.assertEqual(p1,"PMMSE DMWN")
        self.assertEqual(p2,"GOOSE DOWN")
        self.assertEqual(p1.swaps,{"P":"G","M":"O"})
        self.assertFalse(p2.swaps)
        self.assertEqual(p1.mapp,("G","O","O",3,4," ",5,"O",6,7))
        self.assertEqual(p2.mapp,(1,2,2,3,4," ",5,2,6,7))
        lst1 = p1.splitter()
        lst2 = p2.splitter()
        for i1,i2 in zip(lst1,lst2):
            self.assertTrue(i1.swaps)
            self.assertFalse(i2.swaps)
            self.assertTrue(i1.mapp)
            self.assertTrue(i2.mapp)
