# encoding utf-8

class Manager:
    def __init__(self,):
        self.master = None
        self.key = None
        self.cleaned = None
        self._init = None
        self.lst = []
        self.children = []
        self.words = []

    @classmethod
    def mapping(cls,word):
        num,mapp,temps = 0,[],{}
        for i in word:
            if i not in temps:
                mapp.append(num)
                temps[i] = num
                num += 1
            elif i in temps:
                mapp.append(temps[i])
        return mapp
