class InvalidChar(Exception):
    pass

class EndOfTheRope(Exception):
    pass

class Map:
    map_id = 0
    map_keys = {}

    def __init__(self,**kwargs):
        self.phrase_init = kwargs["phrase"]
        self.phrase = kwargs["phrase"]
        self.key = kwargs["key"]
        self.wordset = kwargs["wordset"]
        self.mapseq = {}

    @classmethod
    def stash(cls,key):
        i = str(cls.map_id)
        cls.map_keys[i] = tuple(key.items())
        cls.map_id += 1
        return i

    def analyze(self):
        raise EndOfTheRope

    def key_match(self,word,mapp):
        lst = []
        for part in self.mapseq[mapp]:
            for i,char in enumerate(part):
                if char in self.key:
                    if self.key[char] != word[i]:
                        break
            else:
                lst.append(part)
        return tuple(lst)


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
