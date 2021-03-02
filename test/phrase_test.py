from unittest import TestCase
import os,sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from src.phrase import Phrase,sanatize

class TestPhraseClass(TestCase):

    def setUp(self):
        self.phrase = "PAO XN XNVZ MKPMOZ LMCD JN JAD XNNL PADW JAD XNNLQDKK LTWVZ? TJ'S AMLXKO DYDL UNL JADB."
        self.table = {"X": "D"}

    def test_phrase_initialization(self):
        phrase = Phrase(self.phrase,self.table)
        self.assertIsInstance(phrase,Phrase)
        self.assertEqual(self.phrase,phrase.raw)
        self.assertEqual(self.table,phrase.table)

    def test_phrase_decrypt(self):
        temp = ""
        for char in sanatize(self.phrase):
            if char in self.table:
                temp += self.table[char]
            else:
                temp += char
        phrase = Phrase(self.phrase,self.table)
        decrypted_txt = phrase.decrypt()
        self.assertEqual(temp,decrypted_txt)

    # def test_phrase_split_words(self):
    #     p = sanatize(self.phrase)
    #     phrase = Phrase(self.phrase,self.table)
    #     word_count = len(p.split(" "))
    #     self.assertEqual(word_count,phrase.split_words())

    def test_sanatize(self):
        sanatized = "PAO XN XNVZ MKPMOZ LMCD JN JAD XNNL PADW JAD XNNLQDKK LTWVZ TJ'S AMLXKO DYDL UNL JADB"
        clean_phrase = sanatize(self.phrase)
        self.assertEqual(sanatized,clean_phrase)
