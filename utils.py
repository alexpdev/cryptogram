# Utility functions for cryptogram decryption
from PhraseClass import Phrase

def mapped(word):
    """Generate word map"""
    num,mapp,temps = 0,[],{}
    for i in word:
        if i not in temps:
            mapp.append(num)
            temps[i] = num
            num += 1
        elif i in temps:
            mapp.append(temps[i])
    return mapp

def uniques(code):
    l = []
    for i in code:
        if i.isalpha() and i not in l:
            l.append(i)
    return l

def vowel_idx(phrase,gword,top):
    l = len(phrase)
    pvowels = [i for i in range(l) if phrase[i] in top]
    gvowels = [i for i in pvowels if gword[i] in "AEIOU"]
    if len(gvowels) == len(pvowels):
        return 0
    elif not len(gvowels):
        return 2
    return 1

def split_phrase(phrase):
    """Input: Phrase object sentence
        Output: list of Phrase object words"""
    lst = []
    for word in phrase.split(" "):
        p = Phrase.create(word,phrase.key)
        lst.append(p)
    return lst
