from phrases import Sample,Gwords
from PhraseClass import Phrase
from encrypt import encrypt
import copy

def gfilter(phrase,gwords):
    gset = set()
    for gword in gwords:
        if phrase.is_match(gword):
            gset.add(gword)
    return gset

def matchings(phrase,gwords):
    for gword in gwords:
        if phrase.is_match(gword):
            yield (phrase,gword)

def split_phrase(phrase):
    """Input: Phrase object sentence
        Output: list of Phrase object words"""
    lst,num = [],0
    for word in phrase.split(" "):
        p = Phrase.create(word,phrase.key)
        if p.is_full: num += 1
        else: lst.append(p)
    # s = sorted(lst,key=lambda x: len(x))
    return lst

def solve(phrase,gwords,nlst=[]):
    if len(gwords) == 0:
        return phrase
    lst = split_phrase(phrase)
    for old,new in find_matches(lst,gwords):
        s = phrase.apply_word(old,new)
        # print(phrase.swap)
        # print("BEFORE")
        # print(s.swap)
        g = gfilter(s,gwords)
        p = solve(s,g,nlst)
        nlst.append(p)
        if p.amount() >= len(p) - 60:
            # print("AFTER")
            print(p.swap)
    return phrase

def find_matches(lst,gwords):
    seen = []
    for i,word in enumerate(lst):
        if word in seen:
            continue
        seen.append(word)
        for match in matchings(word,gwords):
            yield match



if __name__ == "__main__":
    phrase = Phrase.create(*Sample)
    solve(phrase,Gwords)
