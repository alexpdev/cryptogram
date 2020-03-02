class InvalidChar(Exception):
    pass

class PhraseMap:
    def __init__(self,phrase,key=None):
        self.phrase = phrase
        self.key = key
        self.partials = self.phrase_split()

    def addKeys(self,part,word):
        chars = []
        for w,p in zip(word,part):
            if p not in self.key:
                self.key[p] = w
                chars.append(p)
        # print("Added",chars,"to",self.key)
        return tuple(chars)

    def removeKeys(self,chars):
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

    def filter_words(self,wordset):
        matches = {}
        self._sort = sorted(self.partials,key=lambda x: len(x.mapp))
        for word,lst in map(self.match,wordset):
            if lst:
                matches[word] = lst
        return matches

    def match(self,word):
        lst = []
        for partial in self._sort:
            if len(partial) < len(word):
                continue
            if len(partial) > len(word):
                break
            word_mapp = Partial(word).mapp
            if partial.mapp == word_mapp:
                lst.append(partial)
        return word,lst

    def gen_partials(self,seq):
        for item in seq:
            yield Partial(item)

    def phrase_split(self):
        seq,lst = self.phrase.split(" "),[]
        for partial in self.gen_partials(seq):
            lst.append(partial)
        return lst

class Partial(str):
    def __init__(self,txt):
        super()
        self.txt = txt
        self._map = None

    @property
    def mapp(self):
        if not self._map:
            self._map = self.mapping(self.txt)
        return self._map

    def mapping(self,word=None):
        word = self if not word else word
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

    def charsInKey(self,key):
        return sum([1 for i in self.txt if i in key])

class Phrase(Partial):
    def __init__(self,phrase):
        super().__init__(phrase)
