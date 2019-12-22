# Utility functions for cryptogram decryption

def mapped(word):
    """Generate word map"""
    num,mapp,temps = 0,[],{}
    for i in word:
        if i not in temps:
            mapp.append(num)
            temps[i] = num
            num += 1
        elif i in temps:
            mapp.append(temps[i])
    return mapp

def normalize(code):
    """Clean code of most punctuation"""
    n_code = [i for i in code if i.isalpha() or i == " "]
    n_code = "".join(n_code).upper()
    return n_code

def positions(word,key):
    """Locations of characters already in key"""
    n_word = normalize(word)
    idx = [i for i in range(len(n_word)) if n_word[i] in key]
    return idx

def amount(word,key):
    """Total amount of swapped characters using key"""
    a = positions(word,key)
    return len(a)

def uniques(code):
    l = []
    for i in code:
        if i.isalpha() and i not in l:
            l.append(i)
    return l

def splt(code):
    """Split cleaned phrase into list of words"""
    n_code = normalize(code)
    lst = n_code.split(" ")
    return lst

def isfull(word,key):
    if amount(word,key) == len(word):
        return True

def isswappy(i,key):
    a = amount(i,key)
    if a > 0 and a < len(i):
        return True
    return False

def isword(i,key,words):
    s = swap(i,key)
    if s in words:
        return True
    return False

def swap(word,key):
    """Returns phrase with applied character swaps from key"""
    if not key:
        return word
    else:
        s = ""
        for i in word:
            if i in key:
                s += key[i]
            else:
                s += i
    return s
