from time import time
from phrases import Gwords,Phrases
from utils import (splt, swap, mapped, uniques,
                    isfull, isswappy, isword)
from encrypt import encypher
# phrase = "ARMY FAR MASTER FIRMLY"
# key,code = encypher(phrase)

def gfilter(code,gwords,key):
    lst = splt(code)
    gset = set()
    for match in find_matches(lst,gwords,key):
        old,new = match
        gset.add(new)
    return gset

def solve(phrase,gwords,key,l,nlst=[]):
    if not gwords:
        return key
    lst = splt(phrase)
    for match in find_matches(lst,gwords,key.copy()):
        old,new = match
        nlst.append(new)
        cpy = key.copy()
        apply_swaps(old,new,cpy)
        g = gfilter(phrase,gwords,cpy)
        gl = len(g)
        nkey = solve(phrase,g,cpy,l,nlst)
        if len(nkey) >= l - 5:
            swp = swap(phrase,nkey)
            if swp not in nlst:
                print(swp)
                nlst.append(swp)
    return key

def apply_swaps(old,new,key):
    for x,y in zip(old,new):
        if x != y and x not in key:
            key[x] = y
    return


def find_matches(lst,gwords,key):
    tlst = []
    for i,txt in enumerate(lst):
        if txt in tlst:
            continue
        tlst.append(txt)
        if len(txt) <= 3:
            continue
        if isfull(txt,key):
            if isword(txt,key,Gwords):
                continue
            else:
                break
        for match in search_words(txt,gwords,key):
            if match:
                yield match

def search_words(txt,gwords,key):
    for gword in gwords:
        if len(gword) == len(txt):
            if is_match(txt,gword,key):
                yield txt,gword

def is_match(txt,gword,key):
    tmapp,gmapp = mapped(txt),mapped(gword)
    if tmapp != gmapp: return False
    for i,char in enumerate(txt):
        g = gword[i]
        if g == char:
            return False
        if g in key.values() and key.get(char) != g:
            return False
        elif char in key and key[char] != g:
            return False
    return True

if __name__ == "__main__":
    for phrase in Phrases:
        then = time()
        gset = gfilter(phrase,Gwords,Phrases[phrase])
        l = len(uniques(phrase))
        print("setup",time() - then)
        then2 = time()
        f = solve(phrase,gset,Phrases[phrase],l)
        print(f)
        print("solve",time() - then2)
        print("solve",time() - then)



# def unapply(temp,key):
#     for i in temp:
#         del key[i]
#     return key
