import os
import sys

root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
words_file = os.path.join(root,"data","words.pickle")
phrase = None #'QIVQOZ QFXQOT QIKQVZ UKKQVZ QIVQKZ'
phrase_path = os.path.join(root,"data","phrases.json")
key = None #{"I":"X"}

verbosity = 1


output = sys.stdout

configuration = {
    "BASE_DIR":root,
    "words_file":words_file,
    "key":key,
    "phrase":phrase,
    "phrase_path":phrase_path,
    "verbosity":verbosity,
    "output":output,
}
