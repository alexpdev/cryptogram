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


if __name__ == "__main__":
    phrase = "MOOSE ROOF FARTHER FIRE FIRST FOREMOST"
    encrypt(phrase)
