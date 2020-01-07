class Phrase(str):

    def __init__(self,s):
        super()
        self.key = {}
        self.top = []

    def __str__(self):
        return self

    @classmethod
    def create(cls,s,key={}):
        s = Phrase.normalize(s)
        phrase = Phrase(s)
        phrase.key = key
        return phrase

    @classmethod
    def normalize(cls,string):
        phrase = ""
        for char in string:
            if char.isalpha():
                phrase += char.upper()
            elif char == " ":
                phrase += char
        return phrase

    @property
    def swap(self):
        """Returns phrase with applied character swaps from key"""
        s = ""
        for char in self:
            if char in self.key:
                s += self.key[char]
            else:
                s += char
        return s

    @property
    def is_full(self):
        pos = self.positions()
        if len(pos) == len(self):
            return True
        return False

    def copy(self):
        k = self.key.copy()
        s = self[:]
        phrase = Phrase.create(s,k)
        return phrase

    def apply_word(self,old,new):
        string = self.copy()
        for i,j in zip(old,new):
            if i not in string.key:
                if j not in string.key.values():
                    string.key[i] = j
        return string

    def trace(self):
        """Generate word map"""
        num,mapp,temps = 0,[],{}
        for i in self:
            if i not in temps:
                mapp.append(num)
                temps[i] = num
                num += 1
            else:
                mapp.append(temps[i])
        return mapp

    def amount(self):
        """Total amount of swapped characters using key"""
        pos = self.positions()
        return len(pos)

    def positions(self):
        """Locations of characters already in key"""
        idx = [i for i in range(len(self)) if self[i] in self.key]
        return idx

    def is_match(self,word):
        """Input: English word uppercase,
        Output: Boolean, self and input are compatible"""
        if len(word) != len(self): return False
        temps = {}
        for c1,c2 in zip(self,word):
            if c1 in self.key:
                if self.key[c1] != c2:
                    return False
            elif c2 in self.key.values():
                return False
            elif c1 in temps and temps[c1] != c2:
                return False
            temps[c1] = c2
        return True

    def analyze_phrase(self):
        counts = {}
        for char in self:
            if not char.isalpha(): continue
            elif char in counts:
                counts[char] += 1
            else:
                counts[char] = 1
        t = list(sorted(counts.items(),key=lambda x: x[1]))
        self.top = t[:4]
        return self.top
