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

    def author_words(self):
        amount = 0
        if "-" in self.raw:
            s = self.raw[(self.raw.index("-")+1):]
            amount = len(s.split(" "))
        return amount

    def decrypt(self):
        temp_txt = ""
        for char in self.txt:
            if char in self.table:
                temp_txt += self.table[char]
            else:
                temp_txt += char
        return temp_txt

    def split_words(self):
        auth_words,parent = self.author_words(),self
        words = self.txt.split(" ")
        for word in words[:]:
            obj = Word(word,parent)
            self.words.append(obj)
        return self.words

    def next_word(self):
        temp, matches = None, None
        for word in self.words:
            if word.matches:
                word.find_matches(word_set=word.matches)
            in_map = [i for i in word.txt if i not in self.table]
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
            if x in self.table and self.table[x] != y:
                return False
            temp_table[x] = y
        self.changes[word] = temp_table
        self.table.update(temp_table)
        return True

    def remove_word(self,word):
        changes = self.changes[word]
        for k,v in changes.items():
            if self.table[k] == v:
                del self.table[k]
        del self.changes[word]
        return


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
