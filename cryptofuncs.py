from phrases import PHRASES,WORDS
from classes import Phrase
from encrypt import encrypt
import copy

def solve(gwords,p,last=""):
    if len(gwords) == 0:    # When there are no words for matching return
        return p.swapper()
    lst = p.splitter()      # list of each word
    matches = get_matches(gwords,lst)
    if not matches:
        return p.swapper()
    finals = []
    for config in configure(p,matches):
        np,ng = config
        swapper = np.swapper()
        finals.append(solve(ng,np))
    return finals

def get_matches(gwords,lst):
    matchings = {}
    for word in lst:
        if len(word.indeces) == len(word):
            continue
        elif word.mapp not in matchings:
            matches = compare(gwords,word)
            if matches:
                matchings[word.mapp] = {'matches':matches,'words':[word]}
        elif word not in matchings[word.mapp]['words']:
            matchings[word.mapp]['words'].append(word)
    return matchings

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

def configure(phrase,matches):
    mp,least = min(matches.items(),key=lambda x: len(x[1]["matches"]))
    first_word = least['words'][0]
    first_matches = least['matches']
    if len(matches[mp]['words']) > 1:
        matches[mp]['words'].remove(first_word)
    else:
        del matches[mp]
    for choice in first_matches:
        uphrase = phrase.update(first_word,choice)
        new_gwords = []
        for v in matches.values():
            new_gwords += list(v['matches'])
        yield (uphrase,set(new_gwords))

if __name__ == "__main__":
    p = "MOOSE ROOF FOREMOST"
    gwords = WORDS
    for i,v in PHRASES.items():
        op = Phrase.create(i,swaps=v)
        print(solve(gwords,op))
    # ep = encrypt(p)
    # for f in solve(gwords,op):
        # print(f)
