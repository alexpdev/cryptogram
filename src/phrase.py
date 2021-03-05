#! /usr/bin/python3
#-*- coding: utf-8 -*-

import json

ALL_WORDS = sorted(json.load(open("data\\allWords.json")),key=len)

def all_words():
    return ALL_WORDS

def sanatize(txt):
    temp = "".join([i for i in txt if i.isalpha() or i in "' "]).replace("  "," ")
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
        for word in self.txt.split(" "):
            obj = Word.new(word,parent=self)
            self.words.append(obj)

    def add_keys(self,old,new):
        changes = {}
        for k,v in zip(old,new):
            if k not in self.table and k.isalpha():
                self.table[k] = v
                changes[k] = v
        self.add_changes(old,new,changes)
        self.find_matches()
        return changes

    def remove_keys(self,match):
        chars = self.changes[match][0]
        for char in chars:
            del self.table[char]
        self.remove_changes(match)
        self.find_matches()
        return chars

    def add_changes(self,old,new,changes):
        self.changes[new] = (changes,old)

    def remove_changes(self,word):
        del self.changes[word]

    def find_matches(self):
        [word.find_matches() for word in self.words]

class Word(str):

    @classmethod
    def new(cls,txt,parent=None):
        word = cls(txt)
        word.setParent(parent)
        word.find_matches()
        return word

    def __init__(self,txt):
        self.txt = txt
        self._parent = None
        self.code = ""
        self.originals = set()
        self.matches = set()
        self.gen_code()

    @property
    def parent(self):
        return self._parent

    def setParent(self,parent):
        self._parent = parent

    def table(self):
        return self._parent.table

    def find_matches(self):
        """
            Find possible matches for the word and stores them in .matches attribute.

            Returns:
                [int]: [total matches]
        """
        if self.originals:
            self.rescan_matches()
        else:
            self.get_matches()
        return len(self.matches)

    def rescan_matches(self):
        for other in self.originals:
            if self.is_match(other):
                self.matches.add(other)
            elif other in self.matches:
                self.matches.remove(other)

    def get_matches(self):
        for word in all_words():
            if len(word) > len(self.txt): break
            if len(word) == len(self.txt) and self.is_match(word):
                self.originals.add(word)
                self.matches.add(word)

    def gen_code(self):
        """
        ### gen_code
        - [generates a code for finding possible matches] \n\n
        ### Returns:
            [str]: [code generated from function]
        """
        start, table = 1, {}
        for char in self.txt:
            if not char.isalpha(): self.code += char
            elif char not in table:
                table[char] = str(start)
                self.code += str(start)
                start += 1
            else: self.code += table[char]
        return self.code

    def is_match(self,other):
        start, code, temp = 1, "", {}
        for i,char in enumerate(other):
            if not self.is_qualified(i,char): return False
            if char == "'": code += char
            elif char in temp: code += temp[char]
            else:
                temp[char] = str(start)
                code += str(start)
                start += 1
        return True if code == self.code else False

    def is_qualified(self,i,new):
        table, old = self.table(), self.txt[i]
        if old == "'" or new == "'":
            return True if old == new else False
        elif old in table:
            return True if table[old] == new else False
        elif new in table.values():
            return False
        return True
