from unittest import TestCase
from decypher import decypher,get_sort
from ranks import ranks

class TestDecypher(TestCase):

    def get_sort_test(self):
        top = get_sort(ranks)
        self.assertEqual(type(top),list)
        self.assertTrue(top)
        self.assertIn("E",top)
