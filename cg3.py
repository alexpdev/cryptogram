from phrases import gwords,Phrases
from utils import amount,positions,splt,swap,mapped,uniques
from encrypt import encypher
# phrase = "ARMY FAR MASTER FIRMLY"
# key,code = encypher(phrase)

def setup(code,gwords,key={}):
    lst = splt(code)
    g = set()
    for pair in get_matches(lst,gwords,key):
        gw,wo = pair
        g.add(gw)
    return g

def solve(code,gwords,key={}):
    if len(gwords) == 0:
        return key
    lst = splt(code)
    l = uniques(code)
    track = []
    for x,y in get_matches(lst,gwords,key):
        if not y: return key
        temp = apply_swaps(x,y,key)
        if not temp: continue
        key.update(temp)
        key = solve(code,gwords,key)
        if len(key) >= len(l)-5:
            print(swap(code,key))
            print(key)
        key = unapply(temp,key)
    return key

def unapply(temp,key):
    for i in temp:
        del key[i]
    return key

def apply_swaps(word1,word2,key):
    temp = {}
    for i,x in enumerate(word1):
        if x not in key:
            temp[x] = word2[i]
        elif key[x] != word2[i]:
            return {}
        elif key[x] == x:
            key = {}
            return key
    return temp


if __name__ == "__main__":
    for i in Phrases:
        g = setup(i,gwords,Phrases[i])
        solve(i,g,Phrases[i])
