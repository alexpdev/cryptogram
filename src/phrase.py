#! /usr/bin/python3
#-*- coding: utf-8 -*-

import json

ALL_WORDS = json.load(open("data\\allWords.json"))

def all_words():
    return ALL_WORDS

def sanatize(txt):
    temp = "".join([i for i in txt if i not in ".?!,:;-\""])
    return temp.replace("  "," ")

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
        words = self.txt.split(" ")
        phrase_object = self
        for word in words:
            obj = Word.create(word,phrase_object)
            self.words.append(obj)
        return self.words

    def add_keys(self,old,new):
        changes = {}
        for k,v in zip(old,new):
            if k not in self.table:
                self.table[k] = v
                changes[k] = v
        self.changes[new] = changes
        self.find_matches()

    def find_matches(self):
        [word.find_matches() for word in self.words]

    def remove_keys(self,match):
        chars = self.changes[match]
        for k,v in chars.items():
            del self.table[k]
        del self.changes[match]
        self.find_matches()
        return chars

    def get_key(self,char):
        for k,v in self.table.items():
            if v == char:
                return k
        return

    def reverse_lookup(self, query, target):
        for key,value in self.table.items():
            if value == query and key != target:
                return False

class Word(str):

    def __init__(self,txt):
        self.txt = txt
        self._parent = None
        self.code = None
        self.raw_matches = set()
        self.matches = set()
        self.find_matches(table={})

    @staticmethod
    def create(txt,parent):
        word = Word(txt)
        word.setParent(parent)
        print(word.parent)
        return word

    def setParent(self,parent):
        self._parent = parent

    def reverse_lookup(self,*args):
        self.parent().reverse_lookup(*args)

    def parent(self):

        return self._parent

    def table(self):
        if not self.parent():
            return self.parent().table.copy()
        return {}

    def find_matches(self,table=None):
        self.gen_code(table=table)
        if table is None:
            self.matches.clear()
            for word in self.explore_words(self.raw_matches):
                self.matches.add(word)
        else:
            word_set = all_words()
            for word in self.explore_words(word_set):
                self.raw_matches.add(word)
            self.matches = self.raw_matches
        return len(self.matches)

    def explore_words(self,word_set):
        for word in word_set:
            if self.compare(word):
                yield word

    def gen_code(self,table=None):
        start, self.code = 1, ""
        if table is None: table = self.table()
        for char in self.txt:
            if char == "'": self.code += "'"
            elif char not in table:
                table[char] = str(start)
                self.code += str(start)
                start += 1
            else: self.code += table[char]
        return self.code

    def compare(self,other):
        if len(self) != len(other): return False
        code, start = "", 1
        table = {} if self.parent() is None else self.parent().table
        for icode,char in zip(self.code,other):
            if icode.isalpha() :
                if char != icode: return False
                code += char
            elif char == "'":
                if icode != "'": return False
                code += "'"
            elif char in table:
                code += table[char]
            elif self.reverse_lookup(char,icode) is False:
                return False
            else:
                table[char] = str(start)
                code += str(start)
                start += 1
        if code != self.code:
            return False
        return True
