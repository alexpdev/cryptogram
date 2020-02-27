import os
import sys
import pickle
import json

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
phrase_file = os.path.join(BASE_DIR,"_words","phrases.json")
words_file = os.path.join(BASE_DIR,"_words","words.pickle")
words = pickle.load(open(words_file,"br"))

phrase = 'QIVQOZ QFXQOT QIKQVZ UKKQVZ QIVQKZ'
# "EXPERT ELDERS EXCEPT ACCEPT EXPECT"
key = {"I":"X"}
# _key = {'E': 'Q', 'X': 'I', 'L': 'F', 'A': 'U', 'P': 'V', 'R': 'O', 'D': 'X', 'S': 'T', 'T': 'Z', 'C': 'K'}

CONFIG = {
    "phrase" : phrase,
    "key" : key,
    "wordset" : words,
}

def cycle():
    phrases = json.load(open(phrase_file,"tr"))
    for phrase in phrases:
        CONFIG["phrase"] = phrase
        CONFIG["key"] = phrases[phrase]
        yield CONFIG
