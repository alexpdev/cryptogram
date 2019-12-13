import copy

class Phrase(str):

    def __init__(self,s):
        super()
        self.swaps = {}
        self.indeces = []
        self.mapp = {}

    def __str__(self):
        return self

    def mapp_split(self):
        if " " not in self:
            return self.mapp
        temps = "".join(str(i) for i in self.mapp).split(", ,")
        mapps = []
        for s in temps:
            mapp = tuple(s.split(','))
            mapps.append(mapp)
        return mapps

    def _word_split(self,word):
        word_swaps = {}
        swaps = self.swaps
        new_word = ""
        for char in word:
            if char == "'":
                new_word += char
            elif char.isalpha():
                if char in self.swaps:
                    word_swaps[char] = self.swaps[char]
                    new_word += char
                else:
                    new_word += char
        phrase = self.create(new_word,word_swaps)
        return phrase

    def splitter(self):
        lst = self.split(" ")
        phrase_lst = []
        for word in lst:
            w = self._word_split(word)
            phrase_lst.append(w)
        return phrase_lst

    def swapper(self):
        swapped = ""
        for char in self:
            if char in self.swaps:
                swapped += self.swaps[char]
            else:
                swapped += char
        return swapped

    def update(self,old_word,new_word):
        swaps = copy.deepcopy(self.swaps)
        for idx in range(len(old_word)):
            if old_word[idx] == new_word[idx]:
                continue
            elif old_word[idx] not in swaps:
                swaps[old_word[idx]] = new_word[idx]
        p = self.create(self,swaps)
        return p

    def swap_indeces(self,swaps=None):
        if not swaps:
            swaps = self.swaps
        return [i for i in range(len(self)) if self[i] in swaps or i == "'"]


    def mapped(self):
        """Ex1 = Phrase("HEQQT WTRQD",swaps={"Q":"L","T":"O"})
            Ex1.mapp = (1,2,"L","L","O"," ",5,"O",6,"L",7)
           Ex2 = Phrase("HEQQT WTRQD")
            Ex2.mapp = (1,2,3,3,4," ",5,4,6,3,7)"""
        num,mapp,pairs = 1,[],{}
        for char in self:
            if char not in pairs:
                if char not in self.swaps:
                    if char in " '":
                        mapp.append(char)
                        pairs[char] = char
                        if char == "'":
                            num += 1
                    else:
                        mapp.append(num)
                        pairs[char] = num
                        num += 1
                elif char in self.swaps:
                    mapp.append(self.swaps[char])
                    pairs[char] = self.swaps[char]
                    num += 1
            elif char in pairs:
                mapp.append(pairs[char])
        return tuple(mapp)


    @classmethod
    def create(cls,s,swaps={}):
        phrase = cls(s)
        phrase.swaps = swaps
        phrase.mapp = phrase.mapped()
        phrase.indeces = phrase.swap_indeces()
        return phrase
