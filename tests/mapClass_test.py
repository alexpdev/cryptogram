from unittest import TestCase
from cryptogram import mapClass
from cryptogram.mapClass import Map
from cryptogram.config import words


class MapTest(TestCase):

    def setUp(self):
        self.words = words
        self.lst = []
        for k,v in EXAMPLES.items():
            kw = {
                "key" : {},
                "phrase": v["code"],
                "final_key":v["final_key"],
                "wordset":self.words,
                "text":k
            }
            self.lst.append(kw)

    def test_create_map(self):
        for kwargs in self.lst:
            mp = Map(**kwargs)
            print(mp.phrase,mp.key)
            self.assertEqual(mp.phrase,kwargs["phrase"])
            self.assertEqual(mp.wordset,kwargs["wordset"])
            self.assertIsInstance(mp,Map)
            self.assertIsInstance(mp.phrase,str)
            self.assertIsInstance(mp.wordset,set)
        return


EXAMPLES = {
    "THAT'S": {
        'code': "LWBH'F",
        'final_key': {
            'L': 'T',
            'W': 'H',
            'B': 'A',
            'H': 'T',
            'F': 'S'
            }
        },
    'HELLO WORLD': {
        'code': 'ZTBYL RWWON',
        'final_key': {
            'Z': 'H',
            'T': 'E',
            'B': 'L',
            'Y': 'L',
            'L': 'O',
            'R': 'W',
            'W': 'O',
            'N': 'D'
            }
        },
    'YOU!': {
        'code': 'SFN!',
        'final_key': {
            'S': 'Y',
            'F': 'O',
            'N': 'U'
            }
        },
    'YOU! FAIL!': {
        'code': 'TQF! UKXI!',
        'final_key': {
            'T': 'Y',
            'Q': 'O',
            'F': 'U',
            'K': 'A',
            'X': 'I',
            'I': 'L'
            }
        }
}
