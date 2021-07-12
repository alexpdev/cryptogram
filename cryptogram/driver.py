#! /usr/bin/python3
#-*- coding: utf-8 -*-

from copy import copy
import json

class Driver:

    def __init__(self,window=None):
        self._window = window
        self._phrase = None
        self.best = 0
        self.changed = False
        self.state = {}

    def __str__(self):
        return self.decrypt()

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
        self.add_changes(word,match)

    def setPhrase(self,phrase):
        self._phrase = phrase

    def decrypt(self):
        text = self.phrase.decrypt()
        self.window.text_browser.append(text)

    def undo_changes(self,match):
        changes = self.phrase.changes[match][0]
        self.window.table.remove_keys(changes)
        self.window.chosen_list.remove_match(match)
        self.phrase.remove_keys(match)

    def add_changes(self,word,match):
        if match not in self.phrase.changes:
            changes = self.phrase.add_keys(word,match)
            self.window.table.add_changes(changes)
            self.window.chosen_list.add_item(match)

    def order_words(self,words):
        return sorted(words,key=lambda x: len(x.matches))

    def auto_solve(self,table):
        self.state.clear()
        self.phrase.table = table
        words = copy(self.phrase.words)
        print(self.solve(words,0))
        json.dump(self.state,open("state.json","wt"))
        return self.best

    def solve(self,words,depth):
        if self.limit_met(words):
            return self.log(depth)
        for word in self.order_words(words):
            if not word.matches: continue
            words.remove(word)
            for match in copy(word.matches):
                self.add_changes(word,match)
                self.decrypt()
                self.window.re_update()
                self.solve(words,depth+1)
                if self.max_best(): return self.log(depth)
                self.undo_changes(match)
            if self.max_best(): return self.log(depth)
            words.append(word)
        return self.log(depth)

    def log(self,depth):
        if self.state and depth <= min(self.state):
            self.best += 1
            print(self.best)
        else:
            self.add_state(depth)
        return self.best

    def add_state(self,depth):
        table, self.best = self.phrase.table, 0
        if depth in self.state:
            self.state[depth].append(table)
        else:
            self.state[depth] = [table]

    def empty_matches(self,words):
        temp = [len(i.matches) for i in words]
        if temp.count(0) > len(words)//2:
            return True
        return False

    def limit_met(self,words):
        if not len(words) or self.max_best() or (
            self.empty_matches(words)):
            return True
        return False

    def max_best(self):
        if self.best > 20:
            print(self.best)
            return True
        return False
