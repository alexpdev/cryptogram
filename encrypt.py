import random
import string

def encrypt(phrase):
    alpha = [i for i in string.ascii_uppercase]
    swaps = {}
    encrypted_phrase = ""
    for char in phrase:
        if char in swaps:
            encrypted_phrase += swaps[char]
        elif not char.isalpha():
            encrypted_phrase += char
        else:
            removed = False
            if char in alpha:
                alpha.remove(char)
                removed = True
            choice = random.choice(alpha)
            swaps[char] = choice
            encrypted_phrase += choice
            alpha.remove(choice)
            if removed:
                alpha.append(char)
    return encrypted_phrase


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
