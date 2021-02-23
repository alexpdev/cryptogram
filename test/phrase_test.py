from unittest import TestCase
from pathlib import Path
import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from src.phrase import Phrase,Word

class TestPhraseClass(TestCase):

    def setUp(self):
        self.phrase = "PAO XN XNVZ MKPMOZ LMCD JN JAD XNNL PADW JAD XNNLQDKK LTWVZ? TJ'S AMLXKO DYDL UNL JADB."
        self.table = {"X": "D"}

    def test_phrase_initialization(self):
        phrase = Phrase(self.phrase,self.table)
        self.assertIsInstance(phrase,Phrase)
        self.assertEqual(self.phrase,phrase.txt)
        self.assertEqual(self.table,phrase.table)
        self.assertEqual(self.words,[])

    def test_phrase_decrypt(self):
        temp = ""
        for char in self.phrase:
            if char in self.table:
                temp += self.table[char]
            else:
                temp += char
        phrase = Phrase(self.phrase,self.table)
        decrypted_txt = phrase.decypt()
        self.assertEqual(temp,decrypted_txt)

    def test_phrase_split_words(self):
        phrase = Phrase(self.phrase,self.table)
        words = [Word(i) for i in self.phrase.split(" ")]
        self.assertEqual(words,phrase.split_words())
        self.assertEqual(words,phrase.words)

