if __name__ == "__main__":
    from mapClass import Map
    from manager import Manager
else:
    from .config import CONFIG
    from .mapClass import Map
    from .manager import Manager

def main(**kwargs):
    mp = Map(**kwargs)
    mp.phrase = sanatize(kwargs["phrase"])
    partials = mp.phrase.split(" ")
    part_map = mp.map_sequence(partials)
    map_dict = mp.filter_words(part_map)
    man = Manager(kwargs["phrase"])
    discover(mp,map_dict,man)
    return man

def discover(mp,map_dict,manager):
    if map_dict:
        pairs,removed = compareMap(mp,map_dict)
        for k in removed:
            del map_dict[k]
        for part,word in pairs:
            chars = mp.addKeys(part,word)
            if manager.log(mp.key): return
            discover(mp,map_dict,manager)
            mp.removeKeys(chars,part)
        map_dict.update(removed)
    return

def compareMap(mp,mapdict):
    mapSrt = sorted(mapdict.items(),key=lambda x: len(x[1]))
    removed,pairs = dict(),[]
    for mapp,words in mapSrt:
        for part in mp.mapseq[mapp]:
            pairs = get_pairs(mp,part,words)
            if not pairs:
                removed[mapp] = words
            else:
                return pairs,removed
    return pairs,removed

def get_pairs(mp,part,words):
    pairs = []
    if not mp.isDecrypt(part):
        for word in words:
            if mp.isMatch(word,part):
                pair = (part,word)
                pairs.append(pair)
    return tuple(pairs)

def sanatize(txt):
    sanatized_txt = ""
    for char in txt:
        if char.isalpha() or char in " '":
            sanatized_txt += char
    return sanatized_txt

if __name__ == "__main__":
    import config
    for kwargs in config.cycle():
        a = main(**kwargs)
        input("Enter to continue")
