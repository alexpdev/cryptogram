# ~*~ charset: utf8 ~*~
# Cryptogram: version 0.1.1
import os
import sys
import json
import pickle

from cryptogram.conf import (version_,PHRASE,KEY,ROOT,
                            WORDS_PATH,PHRASE_PATH,
                            VERBOSITY,INTERACTIVE,OUTPUT)

try:
    from setup import version

    if version == version_:
        from setup import *

except:
    pass

def cycle(phrases,conf):
    for phrase in phrases:
        conf["phrase"] = phrase
        conf["key"] = phrases[phrase]
        yield conf

WORDSET = pickle.load(open(WORDS_PATH,"br"))


confs = {
    "phrase" : PHRASE,
    "key" : KEY,
    "wordset" : WORDSET,
    "verbosity": VERBOSITY,
    "output": OUTPUT,
    "interactive": INTERACTIVE,
}


if PHRASE_PATH:
    phrases = json.load(open(PHRASE_PATH))
    __settings = cycle(phrases,confs)
else:
    __settings = (i for i in [confs])


SETTINGS = __settings
