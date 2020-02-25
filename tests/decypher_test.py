from unittest import TestCase
from cryptogram.decrypt import sanatize

class DecypherTest(TestCase):

    def setUp(self):
        self.samples = {
            "!()^&&$:':;-_a" : "'a",
            "James was Ugly!" : "James was Ugly",
            "ME" : "ME",
            "*******" : "",
            "I'll" : "I'll",
        }


    def test_sanatize(self):
        for k,v in self.samples.items():
            result = sanatize(k)
            print(result,v)
            self.assertEqual(result,v)
