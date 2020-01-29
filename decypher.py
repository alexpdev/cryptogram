from ranks import ranks
from phrases import Phrases

def decypher(phrase,ranks):
    r = get_phrase_rank(phrase)
    top_chars = get_sort(ranks)
    top_phrase = get_sort(r)
    result = solve(phrase,top_chars,top_phrase,{})

def solve(phrase,top_chars,top_phrase,key):
    if not len(top_chars) or not len(top_phrase):
        s = swap(phrase,key)
        return s
    if len(key) == len(top_chars):
        s = swap(phrase,key)
        return s
    for char in top_chars:
        for letter in top_phrase:
            key[letter] = char
            top_chars.remove(char)
            top_phrase.remove(letter)
            solve(phrase,top_chars,top_phrase,key)
            top_chars.append(char)
            top_phrase.append(letter)
            del key[letter]
    s = swap(phrase,key)
    print(s)
    return s

def swap(phrase,key):
    p = ""
    for i in phrase:
        if i in key:
            p += key[i]
        else:
            p += i
    return p


def get_phrase_rank(phrase):
    r = {}
    for i in phrase:
        if i.isalpha():
            if i in r:
                r[i] += 1
            else:
                r[i] = 1
    return r


def get_sort(ranks):
    first = []
    r = ranks.copy()
    l = len(r)
    z = 0
    for k,v in sorted(ranks.items(),key=lambda x:x[1],reverse=True):
        if z < 7:
            first.append(k)
            z += 1
    return first







if __name__ == "__main__":
    for phrase in Phrases:
        decypher(phrase,ranks)
