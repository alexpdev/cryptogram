import json

ALL_WORDS = json.load(open("data\\allWords.json"))

def sanatize(txt):
    temp = "".join([i for i in txt if i not in ".,:{}()-_[]\""])
    return temp

class Phrase:
    def __init__(self,txt,table={}):
        self.raw = txt
        self.txt = sanatize(txt)
        self.table = table
        self.words = []
        self.changes = {}

    def decrypt(self):
        temp_txt = ""
        for char in self.txt:
            if char in self.table:
                temp_txt += self.table[char]
            else:
                temp_txt += char
        return temp_txt

    def split_words(self):
        words = self.txt.split(" ")
        for word in words:
            obj = Word(word)
            self.words.append(obj)
        return self.words

    def next_word(self):
        temp, matches = None, None
        for word in self.words:
            if not word.matches: word.find_matches()
            in_map = [i for i in word if i not in self.table]
            if not in_map: continue
            if not temp or len(word.matches) < matches:
                temp, matches = word, len(word.matches)
        return temp

    def add_word(self,txt,word):
        temp_table = {}
        for x,y in zip(txt,word):
            for item in self.table.items():
                if item[1] == y and item[0] != x:
                    return False
                else: continue
            if x in self.table and self.table[x] != y:
                return False
            temp_table[x] = y
        self.changes[word] = temp_table
        self.table.update(temp_table)

    def remove_word(self,word):
        changes = self.changes[word]
        for k,v in changes.items():
            if self.table[k] == v:
                del self.table[k]
        del self.changes[word]
        return





class Word(str):
    all_words = ALL_WORDS

    def __init__(self,txt):
        self.table = {}
        self.matches = set()
        self.txt = txt
        self.num_map = ""

    def gen_map(self):
        mapping, start = {}, 1
        for char in self.txt:
            new_char,new_start = self.next_char(char,mapping,start)
            self.num_map += new_char
            start = new_start
        return mapping

    def next_char(self,char,mapping,start):
        if char in "'":
            return char, start
        if char in mapping:
            return mapping[char], start
        mapping[char] = str(start)
        return str(start), start +1


    def compare(self,other):
        if len(other) != len(self.txt): return False
        num_map, start, mapping = "", 1, {}
        for char in other:
            new_char,new_start = self.next_char(char,mapping,start)
            num_map += new_char
            start = new_start
            if num_map not in self.num_map:
                return False
        return True

    def find_matches(self):
        if not self.num_map: self.gen_map()
        for word in self.all_words:
            if self.compare(word):
                self.matches.add(word)
        return self.matches
