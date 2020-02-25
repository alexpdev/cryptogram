if __name__ == "__main__":
    from config import CONFIG
    from Mapfuncs import Map
    # from managers import Manager
else:
    from .config import CONFIG
    from .Mapfuncs import Map

def main(**kwargs):
    mp = Map(**kwargs)
    mp.phrase = sanatize(kwargs["phrase"])
    partials = mp.phrase.split(" ")
    part_map = mp.map_sequence(partials)
    word_dict = filter_words(part_map,mp)
    discover(partials,word_dict,mp)

def discover(partials,word_dict,mp):
    if not len(partials):
        return mp.analyze()
    short = find_shortest(word_dict)

def find_shortest(d):
    shortest,mapp = None,None
    for k,v in d.items():
        if not shortest or len(v) < len(shortest):
            shortest = v
            mapp = k
    return mapp

def filter_words(seq,mp):
    lex = dict()
    for word,mapp in mp.gen_map(mp.wordset):
        if mapp in seq:
            if mapp not in lex:
                lex[mapp] = [word]
            else:
                lex[mapp].append(word)
    return lex

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
