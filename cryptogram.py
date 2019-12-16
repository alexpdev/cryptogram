from phrases import WORDS, PHRASES
from classes import Phrase
import string
import random
from encrypt import encypher


def solve(gwords,phrase):
    if not gwords:
        return phrase.swapped
    matches,choices = find_matches(gwords,phrase)
    choice = fewerChoices(choices)
    results = []
    g,p = apply_choice(choice,matches,choices,phrase)
    this = solve(g,p)
    results.append(this)
    return results

def make_choices(lst):
    if len(lst) > 4:
        l = [i for i in lst[:-2] if len(i.indeces) != len(i) and "'" not in i]
    swaps = [len(i.indeces) for i in l]
    length = [len(i) for i in l]
    ml,ms = max(length),max(swaps)
    il,ims = length.index(ml),swaps.index(ms)
    names = l[il],l[ims]
    return names

def find_matches(gwords,phrase):
    choices,lst,matches = {},phrase.splitter(),set()
    names = make_choices(lst)
    for word in lst:
        wm = word.mapp
        if len(word.indeces) != len(word):
            results = get_match(gwords,word)
            if results:
                if word in names:
                    choices[word] = results
                else:
                    matches.update(results)
    return matches,choices

def apply_choice(choice,matches,choices,phrase):
    choice = fewerChoices(choices)
    for i in choices:
        if i != choice:
            matches.update(choices[i])
    if not choices:
        return matches,phrase
    lst = []
    for word in choices[choice]:
        up_phrase = phrase.update(choice,word)
        total_swaps = len(up_phrase.indeces)
        lst.append((word,up_phrase))
    num = 1
    for i in lst:
        print(num,") word, swapped")
        print(i[0],i[1].swapped)
        num += 1
    user = int(input()) - 1
    selection = lst[user]
    return matches,selection[1]




def fewerChoices(choices):
    fewer_choices = ""
    for key in choices:
        if not fewer_choices:
            fewer_choices = key
        elif len(choices[key]) < len(choices[fewer_choices]):
            fewer_choices = key
    return fewer_choices

def get_match(gwords,word):
    gset = set()
    for gword in gwords:
        if gword == "WOODS":
            a = 1
        if len(gword) != len(word):
            continue
        if ismatch(gword,word):
            gset.add(gword)
    return gset

def ismatch(gword,word):
    gmapp = word.Map(word=gword)
    for i in range(len(word)):
        if isinstance(word.mapp[i],str):
            if gword[i] != word.mapp[i]:
                return False
        elif gmapp[i] != word.mapp[i]:
            return False
        elif gword[i] in word.swaps.values():
            return False
    return True

if __name__ == "__main__":
    # phrase = "WOODS"
    for i,j in PHRASES.items():
        p = Phrase.create(i,j)
        results = solve(WORDS,p)
        print(results)
    # key,phrase = encypher(phrase)
    # swaps = {phrase[0] : swap}
