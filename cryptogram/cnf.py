# ~*~ charset: utf8 ~*~
# Cryptogram: version 0.1.1
import os
import sys
import json
import pickle

try:
    from setup import __version__
    if "Cryptogram" not in __version__:
        raise Exception
    from setup import configuration
except:
    from cryptogram.config import configuration

cnf_keys = ["BASE_DIR","words_file","key",
    "phrase","phrase_path","verbosity","output"]

# Instance Settings
BASE_DIR = configuration["BASE_DIR"]
verbosity = configuration["verbosity"]
output = configuration["output"]

words_file = configuration["words_file"]
wordset = pickle.load(open(words_file,"br"))

phrase_path = configuration["phrase_path"]
phrase = configuration["phrase"]
key = configuration["key"]

confs = {
    "phrase" : phrase,
    "key" : key,
    "wordset" : wordset,
    "verbosity": verbosity,
    "output": output,
}

def cycle(phrases,conf):
    for phrase in phrases:
        conf["phrase"] = phrase
        conf["key"] = phrases[phrase]
        yield conf

if phrase_path:
    phrases = json.load(open(phrase_path))
    __settings = cycle(phrases,confs)

SETTINGS = __settings
