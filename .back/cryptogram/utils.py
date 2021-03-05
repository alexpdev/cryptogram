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

import time
from pathlib import Path

WORDS = Path(__file__).resolve().parent / "data" / "allWords.json"
STOP_SIG = False

def discover(matches,pm,window):
    if matches:
        pairs,removed = filter_matches(pm,matches)
        for k in removed:
            del matches[k]
        for part,word in pairs:
            window.add_word(part,word)
            chars = pm.addKeys(part,word)
            discover(matches,pm,window)
            pm.removeKeys(chars)
            window.remove_word(part,word)
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
