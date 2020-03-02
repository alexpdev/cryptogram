from unittest import TestCase
from cryptogram.phraseMap import PhraseMap,InvalidChar
from cryptogram.init import wordset


class PhraseMapTest(TestCase):

    def setUp(self):
        self.words = wordset
        self.phrase = "MYBBP KPQBI"
        self.key = {"M":"H","B":"L"}
        self.maps = [(0,1,2,2,3),(0,1,2,3,4)]

    def test_create_PhraseMap(self):
        pm = PhraseMap(self.phrase,self.key)
        self.assertEqual(pm.phrase,"MYBBP KPQBI")
        self.assertIsInstance(pm,PhraseMap)
        self.assertEqual(pm.key,self.key)

    def test_removeKeys(self):
        pm = PhraseMap(self.phrase,self.key)
        pm.removeKeys(("B","M"))
        self.assertNotIn("B",pm.key)
        self.assertNotIn("M",pm.key)
