#! /usr/bin/python3
#-*- coding: utf-8 -*-

class Driver:

    def __init__(self,window=None):
        self._window = window
        self._phrase = None

    @property
    def window(self):
        return self._window

    @property
    def phrase(self):
        return self._phrase

    def setPhrase(self,phrase):
        self._phrase = phrase

    def solve(self,table):
        self.phrase.table = table
        self.phrase.find_matches()
        new_word_list = self.order_words(self.phrase.words)
        self.solve1(self.phrase,new_word_list)

    def solve1(self,phrase,words):
        if not len(words):
            print("no words")
            return
        for i1,word in enumerate(words[:]):
            print("solving" + ("."*15))
            matches = list(word.matches)
            del words[i1]
            for match in matches:
                phrase.add_keys(word,match)
                self.window.table.add_chars(word,match)
                self.window.text_browser.insert_text(phrase.decrypt())
                self.solve1(phrase,words)
                chars = self.phrase.remove_keys(match)
                self.window.table.remove_keys(chars)
                self.window.re_update()
            words.append(word)
        return

    def order_words(self,words):
        new_list = []
        for word in words:
            if not len(word.matches):continue
            for i,w in enumerate(new_list):
                if len(w.matches) > len(word.matches):
                    new_list.insert(word,i)
                    break
                new_list.append(word)
        return new_list
