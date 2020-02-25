import os
import sys
import pickle
import json

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
phrase_file = os.path.join(BASE_DIR,"_words","phrases.json")
words_file = os.path.join(BASE_DIR,"_words","words.pickle")
words = pickle.load(open(words_file,"br"))
phrases = json.load(open(phrase_file,"tr"))

# phrase = "C QZHK GUZ CXGZQXZG BD SMVU C YZZI ICWZ C'S DX FHPZ DXZ SCIICDX DY GUZ ADQBG NDDW ZTZQ - HECE HXBHQC"
# key = {"W":"K"}
_phrase = "EXPERT ELDERS EXCEPT ACCEPT EXPECT"
_key = {'Q': 'S', 'E': 'Q', 'X': 'I', 'Z': 'R', 'N': 'M', 'W': 'G', 'I': 'C', 'J': 'Y', 'L': 'F', 'A': 'U', 'Y': 'D', 'H': 'P', 'P': 'V', 'M': 'E', 'O': 'J', 'U': 'L', 'R': 'O', 'V': 'B', 'K': 'H', 'B': 'N', 'D': 'X', 'S': 'T', 'F': 'W', 'G': 'A', 'T': 'Z', 'C': 'K'}
phrase = 'QIVQOZ QFXQOT QIKQVZ UKKQVZ QIVQKZ'
key = {"I":"X"}

CONFIG = {
    "phrase" : phrase,
    "key" : key,
    "wordset" : words,
    "examples" : phrases
}
