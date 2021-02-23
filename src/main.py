#!/usr/bin/env python3
from pathlib import Path
import os
import json
import sys
from time import time


PROGRAM_DIR = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
sys.path.append(PROGRAM_DIR)
PHRASES = json.load(open("data\\phrases.json","rt"))

def main():
    for phrase,table in PHRASES.items():
        print(phrase,table)

main()
