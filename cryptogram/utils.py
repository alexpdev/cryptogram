# /usr/bin/python3
# ~*~ charset: utf8 ~*~
# Cryptogram: version 0.1.1
#############################################################################
##
## Copyright (C) 2020 ASPDEV.
##
## Cryptogram v0.1.1
## All rights reserved.
##
## You may use this file under the terms of the GNU AGPLv3 license:
##
## THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
## "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
## LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR
## A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT
## OWNER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL,
## SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT
## LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE,
## DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY
## THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
## (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
## OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE."
##
##
#############################################################################

import json
import time
from pathlib import Path
from cryptogram.phraseMap import PhraseMap

WORDS = Path(__file__).resolve().parent / "data" / "allWords.json"
STOP_SIG = False

def stop_decryption():
    global STOP_SIG
    STOP_SIG = True
    return

def start_decryption(phrase,key,window):
    global STOP_SIG
    STOP_SIG = False
    words = json.load(open(WORDS))
    phrase = sanatize(phrase)
    pm = PhraseMap(phrase,key,window)
    wordset = set(words)
    matches = pm.filter_words(wordset)
    discover(matches,pm,window)

def discover(matches,pm,window):
    if matches:
        if check_end(): return
        window.add_guess(gen_phrase(pm))
        pairs,removed = filter_matches(pm,matches)
        for k in removed:
            del matches[k]
        for part,word in pairs:
            window.add_word(part)
            chars = pm.addKeys(part,word)
            discover(matches,pm,window)
            if check_end(): return
            pm.removeKeys(chars)
            window.remove_word(part)
        matches.update(removed)
        time.sleep(.5)
    return

def filter_matches(pm,matches):
    pairings,removed = {},{}
    for word,partials in matches.items():
        items = find_pairs(pm,word,partials)
        if not items:
            removed[word] = partials
        else:
            for item in items:
                if item not in pairings:
                    pairings[item] = items[item]
                    continue
                pairings[item] += items[item]
    return pairs(pairings),removed

def pairs(pairings):
    srt = sorted(pairings.values(),key=lambda x: len(x))
    lst = []
    for v in srt:
        lst += v
    return tuple(lst)

def find_pairs(pm,word,partials):
    lex = {}
    for partial in partials:
        if pm.isDecrypt(partial): continue
        elif pm.isMatch(word,partial):
            lex[partial] = [(partial,word)]
    return lex

def sanatize(txt):
    clean_txt = ""
    for char in txt:
        if char.isalpha():
            clean_txt += char.upper()
        elif char in ["'"," "]:
            clean_txt += char
    return clean_txt

def gen_phrase(pm):
    p = ""
    for i in pm.phrase:
        if i.isalpha() and i in pm.key:
            p += pm.key[i]
        else:
            p += i
    return p

def check_end():
    if STOP_SIG == True:
        print(STOP_SIG)
        time.sleep(.5)
        return True
