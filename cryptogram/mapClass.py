class InvalidChar(Exception):
    pass

class EndOfTheRope(Exception):
    pass

class Map:

    def __init__(self,**kwargs):
        self.initial = kwargs["phrase"]
        self.phrase = kwargs["phrase"]
        self.key = kwargs["key"]
        self.wordset = kwargs["wordset"]
        self.mapseq = {}

    def addKeys(self,part,word):
        chars = []
        for w,p in zip(word,part):
            if p not in self.key:
                self.key[p] = w
                chars.append(p)
        # print("Added",chars,"to",self.key)
        return tuple(chars)

    def removeKeys(self,chars,part):
        # print("Removing",chars,"from",self.key)
        for i in chars:
            del self.key[i]
        return

    def isDecrypt(self,part):
        for char in part:
            if char not in self.key:
                return False
        return True

    def isMatch(self,word,partial):
        vals = self.key.values()
        for i,char in enumerate(partial):
            if char in self.key:
                if self.key[char] != word[i]:
                    return False
            elif word[i] in vals:
                return False
        return True

    def filter_words(self,seq):
        lex = dict()
        for word,mapp in self.gen_map(self.wordset):
            if mapp in seq:
                if mapp not in lex:
                    lex[mapp] = [word]
                else:
                    lex[mapp].append(word)
        return lex

    def map_sequence(self,seq):
        lst = []
        for item,mapp in self.gen_map(seq):
            lst.append(mapp)
            if mapp in self.mapseq:
                self.mapseq[mapp].append(item)
            else:
                self.mapseq[mapp] = [item]
        return lst

    def gen_map(self,seq):
        for item in seq:
            mapp = self.mapping(item)
            yield item,mapp

    def mapping(self,word):
        num,mapp,temps = 0,[],{}
        for i in word:
            if i.isalpha() and i not in temps:
                mapp.append(num)
                temps[i] = num
                num += 1
            elif i in temps:
                mapp.append(temps[i])
            elif i == "'":
                mapp.append(i)
            else:
                raise InvalidChar
        return tuple(mapp)
