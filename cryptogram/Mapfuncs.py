class InvalidChar(Exception):
    pass

class Map:

    def __init__(self,**kwargs):
        self.phrase_init = kwargs["phrase"]
        self.phrase = kwargs["phrase"]
        self.key = kwargs["key"]
        self.wordset = kwargs["wordset"]
        self.matches = None
        self.sequence = []

    def analyze(self):
        pass

    def filter_words(self,seq,words):
        lex = dict()
        for word,mapp in self.gen_map(words):
            if mapp in seq:
                if mapp not in lex:
                    lex[mapp] = [word]
                else:
                    lex[mapp].append(word)
        self.matches = lex
        return lex

    def map_sequence(self,seq):
        lst = []
        for item,mapp in self.gen_map(seq):
            lst.append(mapp)
        self.mapseq = lst
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
