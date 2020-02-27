from unittest import TestCase
from cryptogram import mapClass
from cryptogram.mapClass import Map,InvalidChar
from cryptogram.config import words


class MapTest(TestCase):

    def setUp(self):
        self.words = words
        self.kwargs = {
            "wordset": self.words,
            "phrase": "MYBBP",
            "key": {"M":"H","B":"L"},
            "mapp": (0,1,2,2,3),
        }
        self.mp = Map(**self.kwargs)

    def test_create_map(self):
        kwargs = self.kwargs
        mp = Map(**kwargs)
        self.assertEqual(mp.phrase,"MYBBP")
        self.assertIsInstance(mp,Map)
        self.assertEqual(mp.key,kwargs["key"])
        self.assertIsInstance(kwargs["key"],dict)

    def test_mapping(self):
        args = ("HI !")
        self.assertRaises(InvalidChar,self.mp.mapping,args)
        self.assertEqual(self.mp.mapping("WHO"),(0,1,2))
        self.assertEqual(self.mp.mapping("MAMMOTH"),(0,1,0,0,2,3,4))
        self.assertIsInstance(self.mp.mapping("MAMMOTH"),tuple)
        self.assertEqual(self.mp.mapping("THEY'RE"),(0,1,2,3,"'",4,2))

    def test_gen_map(self):
        txt = ("HELLO", "WORLD")
        mapgen = self.mp.gen_map(txt)
        self.assertIsInstance(next(mapgen),tuple)
        print(type(mapgen))
        self.assertEqual(next(mapgen),("WORLD",(0,1,2,3,4)))
        del mapgen

    def test_isMatch(self):
        mp = self.mp
        self.assertTrue(mp.isMatch("HELLO",mp.phrase))
        self.assertFalse(mp.isMatch("BAT",mp.phrase))

    def test_isDecrypt(self):
        mp = self.mp
        self.assertFalse(mp.isDecrypt(mp.phrase))
        mp.key.update({"Y":"E","P":"O"})
        self.assertTrue(mp.isDecrypt(mp.phrase))
        mp.key.update({"Y":"E","P":"O","B":"L"})


    def test_addkeys(self):
        mp = self.mp
        mp.addKeys(mp.phrase,"HELLO")
        self.assertEqual(mp.key,{"M":"H","Y":"E","P":"O","B":"L"})
        print(mp.key)

    def test_removeKeys(self):
        mp = self.mp
        mp.removeKeys(("B","M"),mp.phrase)
        self.assertNotIn("B",mp.key)
        self.assertNotIn("M",mp.key)
