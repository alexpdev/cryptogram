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
        self.split_words()

    def decrypt(self):
        temp_txt = ""
        for char in self.txt:
            if char in self.table:
                temp_txt += self.table[char]
            else:
                temp_txt += char
        return temp_txt

    def split_words(self):
        parent = self
        words = self.txt.split(" ")
        for word in words[:]:
            obj = Word(word,parent)
            self.words.append(obj)
        return self.words

    def solve(self):
        word = self.next_word()
        match = next((match for match in word.matches))
        keys = self.add_keys(word,match)
        return word, match, keys

    def add_keys(self,word,match):
        temp_table = {}
        for k,v in zip(word.txt,match):
            if k not in self.table and k != "'":
                temp_table[k] = v
        self.table.update(temp_table)
        self.changes[word.txt] = temp_table
        return temp_table




    def next_word(self):
        temp_word, matches_len = None, None
        for i,word in enumerate(self.words):
            if len(self.words) > 4 and i > len(self.words) -3: continue
            l = len([char for char in word.txt
                    if char in self.table or char == "'"])
            if l == len(word.txt): continue
            word.find_matches()
            if not len(word.matches): continue
            if not temp_word or len(word.matches) < matches_len:
                temp_word = word
                matches_len = len(word.matches)
        return temp_word



class Word:
    all_words = ALL_WORDS

    def __init__(self,txt,parent):
        self.txt = txt
        self.word_code = ""
        self._parent = parent
        self.matches = set()
        self.find_matches()

    def __str__(self):
        return self.txt

    def parent(self):
        return self._parent

    def find_matches(self,word_set=None):
        if not word_set:
            word_set = self.all_words
        self.gen_code()
        self.matches = set()
        for word in word_set:
            if self.compare(word):
                self.matches.add(word)
        return self.matches

    def gen_code(self):
        table,mapping,start = self.parent().table,{},1
        for char in self.txt:
            if char == "'":
                self.word_code += "'"
            if char in table:
                self.word_code += table[char]
            elif char in mapping:
                self.word_code += mapping[char]
            else:
                self.word_code += str(start)
                mapping[char] = str(start)
                start += 1
        return mapping

    def compare(self,other):
        if len(self.txt) != len(other):
            return False
        code, start, mapping = "", 1, {}
        for i,char in enumerate(other):
            txt_i = self.word_code[i]
            if txt_i.isalpha():
                if txt_i != char:
                    return False
                code += char
            elif char == "'":
                code += char
            elif char in mapping:
                code += mapping[char]
            else:
                code += str(start)
                mapping[char] = str(start)
                start += 1
            if code not in self.word_code:
                return False
        return True
