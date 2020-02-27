import random
import string

def encrypt(phrase):
    keys,values,code,key = [],[],"",{}
    alpha = [i for i in string.ascii_uppercase]
    for char in phrase.upper():
        if not char.isalpha():
            code += char
            continue
        elif char in values:
            code += keys[values.index(char)]
            continue
        keys.append(char)
        if char in alpha:
            alpha.remove(char)
            item = random.choice(alpha)
            alpha.append(char)
        else:
            item = random.choice(alpha)
        alpha.remove(item)
        values.append(item)
        code += item
    for k,v in zip(keys,values):
        key[v] = k
    return code,key

def encypher(phrase):
    keys = [i for i in string.ascii_uppercase]
    values = [i for i in string.ascii_uppercase[:]]
    cypher = {" ":" ","'":"'"}
    num,l = 0,len(keys)
    while values:
        char = random.choice(keys)
        temp = []
        if char in values:
            temp.append(char)
            values.remove(char)
        value = random.choice(values)
        cypher[char] = value
        keys.remove(char)
        values.remove(value)
        if temp:
            values += temp
        num += 1
    encrypt = ''.join([cypher[i] for i in phrase])
    return cypher,encrypt

if __name__ == "__main__":
    phrase = "MOOSE ROOF FARTHER FIRE FIRST FOREMOST"
    encrypt(phrase)
    encypher(phrase)
