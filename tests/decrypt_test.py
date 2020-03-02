from unittest import TestCase
from cryptogram.decrypt import sanatize
from cryptogram.phraseMap import PhraseMap

class DecryptTest(TestCase):

    def setUp(self):
        kwargs = {
            "phrase" : 'QFXQOT QIKQVZ UKKQVZ',
            "key" : {"I":"X"},
            "wordset": (
                "EXPECT","ELDERS",
                "EXCEPT","ACCEPT",
                "A","THE","MAN",
                "AFRICA","ASIA")}
        self.kwargs = kwargs
        self.pm = PhraseMap(kwargs["phrase"],kwargs["key"])

    def test_sanatize(self):
        samples = ["HELLO","H!ELLO","WE ARE US",
                   "LET'S FIND OUT","!^&'*#A"]
        for i,x in enumerate(samples):
            txt = sanatize(x)
            l = len(x.split(" "))
            self.assertEqual(len(txt.split(" ")),l)
            if "'" in x:
                self.assertIn("'",txt)
            if i == 4:
                self.assertEqual(txt,"'A")
