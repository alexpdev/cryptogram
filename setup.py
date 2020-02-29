### * Cryptogram 0.0.1 ### * *
### * Setup and Configuration ### * *

import os
import sys

### BASE_DIR: root directory for the Cryptogram program
# BASE_DIR = None
### * words: file containing commonly used words in the english language *
### * the words are used to help decypher the encrypted string *
# words_file = None


### * Phrase: string encrypted the program will attempt to decrypt. *
# phrase = 'QIVQOZ QFXQOT QIKQVZ UKKQVZ QIVQKZ'
### * optionaly you can choose to comment out phrase field above if you *
### * prefer and uncomment and  the phrase_path field below *
# phrase_path = None

### * key: {old:new} to keep track of progress substitutions. *
# key = {"I":"X"}

### * verbosity (0-3) determines the amount of information printed to stdout. *
### * Defaults to 1 which prints the results at certain milestones *
### * Levels 2 and 3 are only reccommended for debugging *
# verbosity = 1

### * output: optionally specify a file to store final results *
# output = sys.stdout


# configuration = {"BASE_DIR":BASE_DIR,"words_file":words_file,"key":key,"phrase":phrase,"phrase_path":phrase_path,"verbosity":verbosity,"output":output}
