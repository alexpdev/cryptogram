import sys,os
from cryptogram.phraseMap import PhraseMap
from cryptogram.manager import Manager,ResetKey,Solved

def main(**kwargs):
    man = Manager(**kwargs)
    key = kwargs["key"]
    wordset = kwargs["wordset"]
    phrase = sanatize(kwargs["phrase"])
    pm = PhraseMap(phrase,key)
    matches = pm.filter_words(wordset)
    discover(matches,pm,man)

def discover(matches,pm,manager):
    if matches:
        pairs,removed = filter_matches(pm,matches)
        for k in removed:
            del matches[k]
        for part,word in pairs:
            chars = pm.addKeys(part,word)
            if manager.log(pm.key): return
            discover(matches,pm,manager)
            pm.removeKeys(chars)
        matches.update(removed)
    return

def filter_matches(pm,matches):
    pairings,removed = {},[]
    for word,partials in matches.items():
        items = find_pairs(pm,word,partials)
        if not items:
            removed.append(word)
        else:
            for item in items:
                if item not in pairings:
                    pairings[item] = items[item]
                    continue
                pairings[item] += items[item]
    return pairs(pairings),removed


def pairs(pairings):
    srt = sorted(pairings.values(),key=lambda x: len(x))
    lst = []
    for v in srt:
        lst += v
    return tuple(lst)

def find_pairs(pm,word,partials):
    lex = {}
    for partial in partials:
        if pm.isDecrypt(partial): continue
        elif pm.isMatch(word,partial):
            lex[partial] = [(partial,word)]
    return lex

def sanatize(txt):
    clean_txt = ""
    for char in txt:
        if char.isalpha():
            clean_txt += char.upper()
        elif char in ["'"," "]:
            clean_txt += char
    return clean_txt
