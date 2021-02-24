#!/usr/bin/env python3
from pathlib import Path
import os
import json
import sys
from time import time
sys.path.append(os.path.abspath(os.path.dirname(os.path.dirname(__file__))))
from src.phrase import Phrase

PHRASES = json.load(open("data\\phrases.json","rt"))
DEBUG = False

def main():
    for phrase,table in PHRASES.items():
        p = Phrase(phrase,table)
        p.split_words()
        word = p.next_word()
        print(word,word.matches)

main()
