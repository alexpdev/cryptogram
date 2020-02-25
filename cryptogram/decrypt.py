if __name__ == "__main__":
    from config import CONFIG
    from Mapfuncs import Map
else:
    from .config import CONFIG
    from .Mapfuncs import Map

def main(**kwargs):
    mp = Map(**kwargs)
    mp.phrase = sanatize(kwargs["phrase"])
    partials = mp.phrase.split(" ")
    part_map = mp.map_sequence(partials)
    map_dict = mp.filter_words(part_map)
    discover(mp,map_dict,[0])

def discover(mp,map_dict,track):
    if not map_dict:
        mp.analyze()
    for pair in get_pairing(mp,map_dict):
        pass


def get_pairing(mp,map_dict):
    mapSrt = sorted(map_dict.items(),key=lambda x: len(x[1]))
    for k,v in mapSrt:
        pair = _pairing(k,v,mp)

def _pairing(mapp,words,mp):
    print (mapp,words,mp.mapseq[mapp])
    partLen,parts = len(mp.mapseq[mapp]),mp.mapseq[mapp]
    wrdLen,vals = len(words),list(mp.key.values())
    keyRev = reverseDict(mp.key)
    pcounts = [sum([1 for j in parts[i] if j in mp.key])
             for i in range(partLen)]
    partial = parts[pcounts.index(max(pcounts))]
    for i,word in enumerate(words):
        for


def reverseDict(key):
    reverse = dict()
    for k,v in key.items():
        reverse[v] = k
    return reverse


    # for partial in mp.mapseq[short]:
    #     matches = mp.key_match(partial,short)
    #     if not matches: continue
    #     first = matches[0]
    #     num = Map.stash(mp.key)

def find_shortest(map_dict):
    shortest,mapp = None,None
    for k,v in map_dict.items():
        if not shortest or len(v) < len(shortest):
            shortest = v
            mapp = k
    return mapp


def sanatize(txt):
    sanatized_txt = ""
    for char in txt:
        if char.isalpha() or char in " '":
            sanatized_txt += char
    return sanatized_txt

if __name__ == "__main__":
    kwargs = CONFIG
    txt = kwargs["phrase"]
    a = main(**kwargs)
    print(a)

# def filter_words(seq,mp):
#     """ Function implemented as method of Map() instance """
#     lex = dict()
#     for word,mapp in mp.gen_map(mp.wordset):
#         if mapp in seq:
#             if mapp not in lex:
#                 lex[mapp] = [word]
#             else:
#                 lex[mapp].append(word)
#     return lex

# def discover(mp,map_dict,track):
#     """ Iterates through words that matched partials in map_dict
#        rather than iterate partials that matched words """
#     if not map_dict:
#         mp.analyze()
#     short = find_shortest(map_dict)
#     for word in map_dict[short]:
#         matches = mp.key_match(word,short)
#         if not matches: continue
#         first = matches[0]
#         num = Map.stash(mp.key)
