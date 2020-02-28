from unittest import TestCase
from cryptogram.decrypt import sanatize
from cryptogram.mapClass import Map

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
        self.mp = Map(**kwargs)

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

        def test_partials(self):
            partials = self.mp.phrase.split(" ")
            part_map = self.mp.map_sequence(partials)
