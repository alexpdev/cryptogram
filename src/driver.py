#! /usr/bin/python3
#-*- coding: utf-8 -*-

class Driver:

    def __init__(self,window=None):
        self._window = window
        self._phrase = None
        self.best = None
        self.changed = False

    def __str__(self):
        return "<instanceof(Driver)>"

    def __repr__(self):
        return self.__str__()

    @property
    def window(self):
        return self._window

    @property
    def phrase(self):
        return self._phrase

    @phrase.setter
    def phrase(self,phrase):
        self.setPhrase(phrase)

    def match_selected(self,word,match):
        changes = self.phrase.add_keys(word,match)
        self.window.table.add_changes(changes)
        self.window.chosen_list.add_item(match)

    def setPhrase(self,phrase):
        self._phrase = phrase

    def decrypt(self):
        text = self.phrase.decrypt()
        self.window.text_browser.append(text)

    def undo_changes(self,match):
        changes = self.phrase.changes[match][0]
        self.window.table.remove_keys(changes)
        self.phrase.remove_keys(match)

    def decrypt_count(self):
        return len([i for i in self.phrase.txt if i in self.phrase.table and i not in " '"])

    def solve(self,table):
        self.phrase.table = table
        self.phrase.find_matches()
        new_word_list = self.order_words(self.phrase.words)
        print(new_word_list)
        self.solve1(self.phrase,new_word_list)

    def solve1(self,phrase,words):
        for i,word in enumerate(words):
            del words[i]
            matches = list(word.matches)
            print(matches)
            for match in matches:
                changes = phrase.add_keys(word,match)
                self.window.table.add_changes(changes)
                self.window.chosen_list.add_item(match)
                self.window.text_browser.append(phrase.decrypt())
                self.window.re_update()
                self.solve1(phrase,words)
                self.window.chosen_list.remove_match(match)
            words.append(word)
        return

    def order_words(self,words):
        temp = [i for i in words if len(i.matches) > 0]
        return sorted(temp,key=lambda x: len(x.matches))
