from unittest import TestCase
import os,sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from cryptogram.phrase import Phrase,sanatize

class TestPhraseClass(TestCase):

    def setUp(self):
        self.phrase = "WMEEL KLIEP. RWYC YC FV MGFDAEM."
        self.table = {"R": "T"}

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

    def test_sanatize(self):
        sanatized = "WMEEL KLIEP RWYC YC FV MGFDAEM"
        clean_phrase = sanatize(self.phrase)
        self.assertEqual(sanatized,clean_phrase)

    def test_add_keys(self):
        phrase = Phrase(self.phrase,self.table)
        phrase.add_keys("YC","IS")
        self.assertIn("Y",phrase.table)
        self.assertIn("C",phrase.table)
        self.assertEqual(phrase.table["Y"],"I")
        self.assertEqual(phrase.table["C"],"S")
        self.assertIn("IS",phrase.changes)
        self.assertEqual(phrase.changes['IS'], ({'Y':'I','C':'S'},'YC'))
        phrase.add_keys('RWYC','THIS')
        for c1,c2 in zip('RWYC','THIS'):
            self.assertIn(c1,phrase.table)
            self.assertEqual(phrase.table[c1],c2)
        self.assertIn('THIS',phrase.changes)
        self.assertEqual(phrase.changes['THIS'], ({'W':'H'},'RWYC'))
        phrase.add_keys('WMEEL','HELLO')
        for c1,c2 in zip('WMEEL','HELLO'):
            self.assertIn(c1,phrase.table)
            self.assertEqual(phrase.table[c1],c2)
        self.assertIn('HELLO',phrase.changes)
        self.assertEqual(phrase.changes['HELLO'], ({'M':'E','L':'O','E':'L'},'WMEEL'))
        phrase.add_keys('MGFDAEM','EXAMPLE')
        for c1,c2 in zip('MGFDAEM','EXAMPLE'):
            self.assertIn(c1,phrase.table)
            self.assertEqual(phrase.table[c1],c2)
        self.assertIn('EXAMPLE',phrase.changes)
        self.assertEqual(phrase.changes['EXAMPLE'], ({'G':'X','F':'A','D':'M','A':'P'},'MGFDAEM'))

    def test_remove_keys(self):
        pairs = [("YC","IS"),('RWYC','THIS'),('WMEEL','HELLO'),('MGFDAEM','EXAMPLE')]
        phrase = Phrase(self.phrase,self.table)
        for pair in pairs: phrase.add_keys(*pair)
        for pair in pairs:
            changes = phrase.changes[pair[1]]
            phrase.remove_keys(pair[1])
            self.assertNotIn(pair[1],phrase.changes)
            for char in changes:
                self.assertNotIn(char,phrase.table)







