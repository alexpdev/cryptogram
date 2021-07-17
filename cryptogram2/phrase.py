import os
import json

def get_wordset():
    path = os.path.join(os.getcwd(), "data", "allWords.json")
    data = json.load(open(path))
    wordset = sorted(set(data), key=len)
    return wordset

class Data:
    wordset = get_wordset()

class Phrase:

    wordset = Data.wordset

    def __init__(self,phrase,key=None):
        self.phrase = phrase
        self.key = key
        self.children = []
        self.selected_words = []

    def gen_words(self):
        for word in self.phrase:
            word_map = self.get_int_map(word)
            child = Word(word, word_map, parent=self)
            self.children.append(child)


    def get_int_map(self, word):
        mapping, translation, counter = {}, [], 1
        for item in word:
            if item in mapping:
                translation.append(mapping[item])
            else:
                mapping[item] = counter
                counter += 1
        return mapping


class Word(Phrase):

    def __init__(self, word, word_map, parent=None):
        self.parent = parent
        self.word = word
        self.word_map = word_map
        self.used_words = []

    @property
    def key(self):
        if self.parent:
            return self.parent.key
        if hasattr(self,"_key"):
            return self._key
        self._key = {}
        return self._key

    @key.setter
    def set_key(self,char,num):
        self.key[char] = num

    def _next_word(self):
        string = self.matches[0]
        self.used_words.append(string)
        del self.matches[0]
        return string

    def translate_word(self):
        string = self._next_word()
        for num,char in zip(self.word, string):
            if self._test_key(num,char):
                self.set_key(num,char)
        return self.key

    def _test_key(self,num,char):
        if num in self.key:
            if self.key.get(num) == char:
                return True
            return False
        if char in self.key.values():
            return False

    def filter_wordset(self, word_map):
        for string in self.wordset:
            if len(string) == len(word_map):
                if string not in self.wordset_mappings:
                    string_word_map = self.get_int_map()
                    self.wordset_mappings[string] = string_word_map
                else:
                    string_word_map = self.worddata_mappings[string]
                if string_word_map == word_map:
                    yield string
