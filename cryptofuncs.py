from phrases import Sample,Gwords
from PhraseClass import Phrase
from utils import vowel_idx,split_phrase
from encrypt import encrypt
import copy


def solve(phrase,gwords,nlst=[]):
    if len(gwords) == 0: return phrase
    lst = split_phrase(phrase)
    for old,new in matchings(lst,gwords):
        temp = phrase.copy()
        temp = temp.apply_word(old,new)
        new_phrase = solve(temp,gwords,nlst)
        swap = new_phrase.swap
        if swap not in nlst:
            nlst.append(swap)
            print(swap)



def matchings(lst,gwords):
    seen = []
    for word in lst:
        if word.is_full or word in seen:
            continue
        seen.append(word)
        for gword in gwords:
            if word.is_match(gword):
                yield word,gword

def gfilter(phrase,gwords):
    top = phrase.analyze_phrase()
    lst,seen = split_phrase(phrase),[]
    first,second,third = set(),set(),set()
    sets = [first,second,third]
    for word in lst:
        if word in seen or word.is_full:
            continue
        seen.append(word)
        for gword in gwords:
            if word.is_match(gword):
                idx = vowel_idx(word,gword,top)
                sets[idx].add(gword)
    for gs in sets:
        if gs: yield gs


if __name__ == "__main__":
    phrase = Phrase.create(*Sample)
    for gwords in gfilter(phrase,Gwords):
        phrase = solve(phrase,gwords)
