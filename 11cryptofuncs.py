from phrases import PHRASES,WORDS
from classes import Phrase
from encrypt import encrypt
import copy

def solve(gwords,p,finals=[]):
    if not gwords:
        return p
    lst = p.splitter()      # list of each word
    matches,lword = get_matches(gwords,lst)
    if not matches:
        return p
    for config in configure(p,matches,lword):
        gset,nphrase = config
        swapper = nphrase.swapped
        finals.append(solve(gset,nphrase))
    return finals

def get_matches(gwords,lst):
    matchings,least,lword = {},0,""
    for word in lst:
        if len(word.indeces) == len(word):
            continue
        elif "'" in word:
            continue
        elif word.mapp not in matchings:
            matches = compare(gwords,word)
            if matches:
                if not least or len(matches) < least:
                    least,lword = len(matches),word
                matchings[word.mapp] = {'matches':matches,'word':word}
    return matchings,lword

def compare(gwords,word):
    matches = set()
    for g in gwords:
        if len(g) == len(word):
            gphrase = Phrase.create(g)
            if ismatch(gphrase,word):
                matches.add(gphrase)
    return matches

def ismatch(gphrase,word):
    for pos in range(len(word)):
        if type(word.mapp[pos]) == type(pos):
            if word.mapp[pos] != gphrase.mapp[pos]:
                return False
        elif word.mapp[pos].isalpha():
            if word.mapp[pos] != gphrase[pos]:
                return False
    return True

def configure(phrase,matches,lword):
    lkey = lword.mapp
    for match in matches[lkey]['matches']:
        nphrase = phrase.update(lword,match)
        gset = []
        for k in matches:
            if k != lkey:
                gset += list(matches[k]['matches'])
        gset = set(gset)
        yield gset,nphrase



if __name__ == "__main__":
    p = "MOOSE ROOF FOREMOST"
    gwords = WORDS
    for i,v in PHRASES.items():
        op = Phrase.create(i,swaps=v)
        print(solve(gwords,op))
    # ep = encrypt(p)
    # for f in solve(gwords,op):
        # print(f)
