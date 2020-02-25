from __init__ import CONFIG
from Mapfuncs import Map
# from managers import Manager,Phrase

def main(**kwargs):
    mp = Map()
    phrase = sanatize(kwargs["phrase"])
    partials = phrase.split(" ")
    part_map = mp.map_sequence(partials)
    words = kwargs["wordset"]
    word_dict = filter_words(mp,part_map,words)
    print(word_dict)

def filter_words(mp,seq,words):
    lex = dict()
    for word,mapp in mp.gen_map(words):
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
