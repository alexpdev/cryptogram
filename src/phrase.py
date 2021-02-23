import json

ALL_WORDS = json.load(open("data\\allWords.json"))

class Phrase:
    def __init__(self,txt,table={}):
        self.txt = txt
        self.table = table
        self.words = []

    def decrypt(self):
        temp_txt = ""
        for char in self.txt:
            if char in self.table:
                temp_txt += self.table[char]
            else:
                temp_txt += char
        print(temp_txt)
        return temp_txt

    def split_words(self):
        words = self.txt.split(" ")
        for word in words:
            self.words.append(Word(word))
        return self.words



class Word(str):
    all_words = ALL_WORDS

    def __init__(self,txt):
        self.table = {}
        self.txt = txt
        self.matches = set()
        self.numer_map = ""

    def gen_map(self):
        mapping, start = {}, 1
        for char in self.txt:
            new_char,new_start = self.next_char(char,mapping,start)
            self.number_map += new_char
            start = new_start
        return mapping

    def next_char(self,char,mapping,start):
        if char in "'.":
            return char, start
        if char in mapping:
            return mapping[char], start
        mapping[char] = str(start)
        return str(start), start +1


    def compare(self,other):
        if len(other) != len(self.txt): return False
        number_map, start, mapping = "", 1, {}
        for char in other:
            new_char,new_start = self.next_char(char,mapping,start)
            number_map += new_char
            start = new_start
            if number_map not in self.number_map:
                return False
        return True

    def find_matches(self):
        if not self.number_map: self.gen_map()
        for word in self.all_words:
            if self.compare(word):
                self.matches.add(word)
        return self.matches
