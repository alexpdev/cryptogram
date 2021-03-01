#! /usr/bin/python3
#-*- coding: utf-8 -*-

class Driver:

    def __init__(self,window=None):
        self._window = window

    @property
    def window(self):
        return self._window

    def solve(self,phrase):
        words = phrase.words
        new_word_list = self.order_words(words)
        self.solve1(phrase,new_word_list)

    def solve1(self,phrase,words):
        if not len(words):
            return
        for i1,word in enumerate(words[:]):
            matches = list(word.matches)
            del words[i1]
            for match in matches:
                phrase.add_keys(word,match)
                self.window.table.add_chars(word,match)
                self.window.text_browser.insert_text(phrase.decrypt())
                self.solve1(phrase,words)
                chars = self.phrase.remove_keys(match)
                self.window.table.remove_keys(chars)
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
