#! env/Scripts/python
# -*- coding: utf-8 -*-

import json

def script():
    end = "Q"
    back = "B"
    exit_trigger = False
    phrase = []
    print(f"1: enter next integer of the word sequennce\n2: Enter a ',' seperated list of integers representing a whole word. \n3: Ennter '{end}' to quit and return results. \n4: Enter '{back}' to undo last entry. \n5:Enter ' ' or no input at all to represent ending a word and the next input will be the start of a new word")
    word = []
    count = 0
    while exit_trigger == False:
        phrase_len = len(phrase)
        inp = input(f"(Int,{end},{back},''):")
        if "," in inp:
            word = [int(x) for x in inp.split(",")]
            phrase.append(word)
            word = []
        elif inp.isnumeric():
            word.append(int(inp))
        elif list(filter(lambda x: x != ' ',inp)) == []:
            phrase.append(word)
            word = []
        elif inp == end:
            phrase.append(word)
            print(phrase)
            json.dump(phrase,open("out.json","wt"))
            print("output to out.json")
            exit_trigger = True
        elif inp == back:
            if len(word) > 0:
                del word[-1]
            else:
                word = phrase[-1][:]
                del phrase[-1]
        if len(phrase) > phrase_len:
            print("phrase: ",phrase)
    return phrase

if __name__ == '__main__':
    phrase = script()
