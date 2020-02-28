import random
import string

def encrypt(phrase):
    """encrypts string with randomly generated character
    substitution cypher. returns encrypted text and key"""
    alpha,cv,vc = [i for i in string.ascii_uppercase],{},{}
    txt = ""
    for char in phrase.upper():
        if char in vc:
            txt += vc[char]
        elif char.isalpha():
            if char in alpha:
                alpha.remove(char)
                let = random.choice(alpha)
                alpha.append(char)
            else:
                let = random.choice(alpha)
            alpha.remove(let)
            vc[char] = let
            cv[let] = char
            txt += let
        else:
            txt += char
    return txt,cv

def apply_cypher(phrase,cypher):
    """ encrypts string using given key previously generated
    by gen_cypher function and returns encrypted text """
    encrypted,r = "",reverse_dict(cypher)
    for i in phrase.upper():
        if i.isalpha():
            encrypted += r[i]
        else:
            encrypted += i
    return encrypted

def reverse_dict(dct):
    """ reverses dictionary; e.g. k:v --> v:k """
    reversed = {}
    for k,v in dct.items():
        reversed[v] = k
    return reversed


def gen_cypher():
    """ Creates a random charachter substitution cypher for
    the entire alphabet and returns it as a dictionary """
    alpha = [i for i in string.ascii_uppercase]
    beta, start, dct = alpha[:], 0, dict()
    while start < len(beta):
        val,r = beta[start],False
        if val in alpha:
            alpha.remove(val)
            r = True
        char = random.choice(alpha)
        dct[char] = val
        alpha.remove(char)
        if r:
            alpha.append(val)
            r = False
        start += 1
    return dct

if __name__ == "__main__":
    pass
    # phrase = "MOOSE ROOF FARTHER FIRE FIRST FOREMOST"
