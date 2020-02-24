# encoding utf-8

class PhraseManager:
    def __init__(self,words,phrase,key):
        self.origin = phrase
        self.key = key
        self.words = words
        self.kws = {}

    def mapping(self,word):
        num,mapp,temps = 0,[],{}
        for i in word:
            if i not in temps:
                mapp.append(num)
                temps[i] = num
                num += 1
            elif i in temps:
                mapp.append(temps[i])
        return mapp

    def filter_options(self):
        pass
