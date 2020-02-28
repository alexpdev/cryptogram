import string
from unittest import TestCase
from cryptogram.encrypt import (gen_cypher,
                                encrypt,
                                apply_cypher,
                                reverse_dict)

class EncryptTest(TestCase):

    def test_gen_cypher(self):
        key = gen_cypher()
        self.assertEqual(len(key),26)
        for i in string.ascii_uppercase:
            self.assertIn(i,key)
            self.assertIn(i,key.values())
            self.assertNotEqual(i,key[i])

    def test_apply_cypher(self):
        key = gen_cypher()
        phrase = "HOW NOW BROWN COW"
        txt = apply_cypher(phrase,key)
        for i,x in enumerate(phrase):
            if x == " ":
                self.assertEqual(x,txt[i])
            else:
                self.assertNotEqual(x,txt[i])
                self.assertEqual(key[txt[i]], x)

    def test_encrypt(self):
        phrase = "HOW NOW BROWN COW"
        txt,key = encrypt(phrase)
        self.assertIsInstance(txt,str)
        self.assertIsInstance(key,dict)
        for i,x in enumerate(txt):
            if x == " ":
                self.assertEqual(x,phrase[i])
            else:
                self.assertEqual(key[x],phrase[i])
