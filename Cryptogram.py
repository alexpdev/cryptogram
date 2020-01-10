from phrases import Sample,Gwords
from PhraseClass import Phrase
from utils import split_phrase,uniques
from encrypt import encrypt
import copy

def set_up(phrase,gwords):
    nlst = []
    lst = split_phrase(phrase)
    result = solve(phrase,gwords,nlst,lst)

def solve(phrase,gwords,nlst,lst):
    if not len(lst):
        return phrase
    if not len(gwords):
        l = uniques(phrase)
        if len(phrase.key) > len(l) - 7:
            print(nlst,lst,phrase.key)
            print(phrase.swap)
        return phrase
    p = phrase.copy()
    for old,new in get_matches(lst,gwords):
        phrase = phrase.apply_key(old,new)
        nlst.append(new)
        lst.remove(old)
        new_words = gfilter(phrase,gwords)
        temp = solve(phrase,new_words,nlst,lst)
        nlst.remove(new)
        lst.append(old)
        phrase = p
    return phrase


def check_phrase(phrase,gwords):
    a,b = len(gwords),phrase.key
    p_lst = split_phrase(phrase)
    num = 0
    for word in p_lst:
        a = word.key
        if word.isfull:
            continue
        else:
            swap = word.swap
            if word.swap not in gwords:
                num += 1
    if num > 4:
        return False
    return True

def get_matches(lst,gwords):
    seen = []
    for word in lst:
        a,b = len(gwords),phrase.key
        if len(word) < 3: continue
        if word in seen: continue
        if word.isfull: continue
        seen.append(word)
        for match in matchings(word,gwords):
            if match:
                yield match

def gfilter(phrase,gwords):
    a,b = len(gwords),phrase.key
    p_lst,gset = split_phrase(phrase),set()
    seen = []
    for word in p_lst:
        if word in seen:continue
        seen.append(word)
        for match in matchings(word,gwords):
            if match:
                gset.add(match[1])
    return gset

def matchings(word,gwords):
    for gword in gwords:
        if word.is_match(gword):
            yield word,gword

if __name__ == "__main__":
    phrase = Phrase.create(*Sample)
    gwords = gfilter(phrase,Gwords)
    phrase = set_up(phrase,gwords)
