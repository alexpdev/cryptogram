import json
import os
from pathlib import Path
from cryptogram2.phrase import Phrase

def main():
    p = Path(os.getcwd())
    phrases = json.loads((p/"data"/"phrases2.json").read_text())

    for phrase,key in phrases:
        print(phrase,key)
        p = Phrase(phrase,key)
        p.gen_words()
        print(p)
        print(p.key, p.children)
