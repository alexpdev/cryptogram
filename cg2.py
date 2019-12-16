from phrases import WORDS, PHRASES
from classes import Phrase
import string
import random
from encrypt import encypher


def solve(gwords,phrase):
    if not gwords:
        return phrase
    matches,pairs = find_matches(gwords,phrase)
    if not matches:
        return phrase
    results = None
    for pair in pairs:
        n_phrase = phrase.update(pair[1],pair[0])
        if not results:
            results = solve(matches,n_phrase)
        else:
            r = solve(matches,n_phrase)
            if len(results.swapps) > r.swapps:
                del n_phrase
                continue
            else:
                results = r
        print(result.swapped,len(result.indeces))
    return results

def find_matches(gwords,phrase):
    matches,pairs = set(),set()
    lst = [i for i in phrase.splitter() if "'" not in i and len(i.indeces) != len(i)]
    for word in lst:
        results,twos = get_match(gwords,word)
        if results:
            matches.update(results)
            pairs.update(twos)
    return matches,pairs

def get_match(gwords,word):
    gset = set()
    pair = set()
    for gword in gwords:
        if gword == "WOODS":
            a = 1
        if len(gword) != len(word):
            continue
        if ismatch(gword,word):
            gset.add(gword)
            pair.add((gword,word))
    return gset,pair

def ismatch(gword,word):
    gmapp = word.Map(word=gword)
    for i in range(len(word)):
        if isinstance(word.mapp[i],str):
            if gword[i] != word.mapp[i]:
                return False
        elif gmapp[i] != word.mapp[i]:
            return False
        elif gword[i] in word.swaps.values():
            return False
    return True

if __name__ == "__main__":
    # phrase = "WOODS"
    for i,j in PHRASES.items():
        p = Phrase.create(i,j)
        results = solve(WORDS,p)
        print(results)
    # key,phrase = encypher(phrase)
    # swaps = {phrase[0] : swap}
