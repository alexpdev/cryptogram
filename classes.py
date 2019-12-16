import copy

class MapMixin:

    def Map(self,word=""):
        word = word if word else self
        p = "".join([i for i in word if i.isalpha() or i in " '"])
        seen,mapp,num = {},[],1
        for char in p:
            if char in seen:
                mapp.append(seen[char])
            elif char in self.swaps:
                mapp.append(self.swaps[char])
                seen[char] = self.swaps[char]
                num += 1
            elif char in " '":
                mapp.append(char)
                num += 1 if char == "'" else num
            elif char.isalpha():
                seen[char] = num
                mapp.append(num)
                num += 1
        return tuple(mapp)

    def map_split(self):
        if " " not in self:
            return self.mapp
        temps = "".join(str(i) for i in self.mapp).split(", ,")
        mapps = []
        for s in temps:
            mapp = tuple(s.split(','))
            mapps.append(mapp)
        return mapps

class Phrase(str,MapMixin):

    def __init__(self,s):
        super()
        self.swaps = {}
        self.indeces = []
        self.swapped = ""
        self.mapp = {}

    def __str__(self):
        return self

    @classmethod
    def create(cls,s,swaps={}):
        phrase = cls(s)
        phrase.swaps = swaps
        phrase.mapp = phrase.Map()
        phrase.swapped = phrase.swapper()
        phrase.indeces = phrase._swap_indeces()
        return phrase


    def splitter(self):
        p = "".join([i for i in self if i.isalpha() or i in " '"])
        lst = p.split(" ")
        phrase_lst = []
        for word in lst:
            w = self.create(word,self.swaps)
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

    def _swap_indeces(self):
        rng = range(len(self))
        return [i for i in rng if self[i] in self.swaps or self[i] == "'"]
