class Phrase(str):

    def __init__(self,s):
        str.__init__(self,s)
        self.d = dict()

    def __str__(self):
        return self

    def swap(self):
        lst = []
        for i in self:
            if i in self.d:
                lst.append(self.d[i])
            else:
                lst.append(i)
        return "".join(lst)

    def words(self):
        lst = self.split(" ")
        seq = []
        for i in lst:
            word = Phrase.create(i,self.d)
            seq.append(word)
        return seq

    def is_full(self):
        for i in self:
            if i not in self.d:
                return False
        return True

    def trace(self,word=None):
        temp,num,lst = dict(),0,[]
        word = self if not word else word
        for i in word:
            if i in temp:
                lst.append(temp[i])
            else:
                lst.append(num)
                temp[i] = num
                num += 1
        return lst

    def compare(self,word):
        if len(word) != len(self): return False
        if self.trace() != self.trace(word): return False
        for i,j in zip(self,word):
            if i in self.d:
                if self.d[i] != j:
                    return False
            elif j in self.d.values():
                return False
        return True

    @classmethod
    def create(cls,s,k):
        s = "".join([i.upper() for i in s if i.isalpha() or i == " "])
        phrase = Phrase(s)
        phrase.d = k
        return phrase
