from time import time
from phrases import Gwords,Phrases
from phrases import p
from utils import (splt, swap, mapped, uniques,
                    isfull, isswappy, isword)
from encrypt import encypher
# phrase = "ARMY FAR MASTER FIRMLY"
# key,code = encypher(phrase)

def gfilter(code,gwords,key={}):
    lst = splt(code)
    gset = set()
    for match in find_matches(lst,gwords,key):
        old,new = match
        gset.add(new)
    return gset

def solve(phrase,gwords,l,key={},nlst=[]):
    if not gwords:
        return key.copy()
    lst = splt(phrase)
    for match in find_matches(lst,gwords,key.copy()):
        old,new = match
        nlst.append(new)
        cpy = apply_swaps(old,new,key.copy())
        g = gfilter(phrase,gwords,cpy)
        gl = len(g)
        nkey = solve(phrase,g,l,cpy.copy(),nlst)
        if len(nkey) >= l - 6:
            swp = swap(phrase,nkey)
            if swp not in nlst:
                print(swp)
                nlst.append(swp)
    return key.copy()

def apply_swaps(old,new,key):
    for x,y in zip(old,new):
        if x != y and x not in key:
            key[x] = y
    return key


def find_matches(lst,gwords,key):
    tlst = []
    for i,txt in enumerate(lst):
        if txt in tlst:
            continue
        tlst.append(txt)
        if isfull(txt,key):
            if isword(txt,key,Gwords):
                continue
            else:
                break
        for match in search_words(txt,gwords,key):
            if match:
                yield match

# def search_words(txt,gwords,key):
#     for gword in gwords:
#         if len(gword) == len(txt):
#             if is_match(txt,gword,key):
#                 yield txt,gword

# def is_match(txt,gword,key):
#     tmapp,gmapp = mapped(txt),mapped(gword)
#     if tmapp != gmapp: return False
#     for i,char in enumerate(txt):
#         g = gword[i]
#         if g == char:
#             return False
#         if g in key.values() and key.get(char) != g:
#             return False
#         elif char in key and key[char] != g:
#             return False
#     return True

if __name__ == "__main__":
    then = time()
    keys = {"L":"Y","S":"N","Q":"E","V":"W","M":"A","T":"S","Y":"R","N":"O","G":"L","P":"U","F":"T","E":"I"}
    gset = gfilter(p,Gwords,keys)
    l = len(uniques(p))
    print("setup",time() - then)
    then2 = time()
    f = solve(p,gset,l,keys)
    print(f)
    print("solve",time() - then2)
    print("solve",time() - then)



# def unapply(temp,key):
#     for i in temp:
#         del key[i]
#     return key
