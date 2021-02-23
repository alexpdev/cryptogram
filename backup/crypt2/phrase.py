P = "HELLO WORLD"

class Phrase:

    def __init__(self,phrase):
        self.phrase = phrase
        self.words = []
        self.trans = {}
        self.mapping = ""

    def split(self):
        for i in self.phrase.split(" "):
            word = Word(i,self)
            self.words.append(word)

    def get_matches(self,words):
        for word in self.words:
            word.match(words)
        return

    def next_word(self):
        matches,sword = None,None
        for word in self.words:
            if len([i for i in self.trans if i in word]) == len(word):
                continue
            if len(word.word) == 2:
                return word
            if not matches:
                matches = len(word.matches)
                sword = word
            else:
                if len(word.matches) < matches:
                    matches = len(word.matches)
                    sword = word
        return sword





class Word:
    def __init__(self,parent,word):
        self.parent = parent
        self.word = word
        self.mapped = ""
        self.matches = set()

    def mapping(self):
        m,start = {},0
        for char in self.word:
            if char in "'.":
                self.mapped += char
            elif char in m:
                self.mapped += m[char]
            else:
                m[char] = str(start)
                self.mapped += str(start)
                start += 1
        return self.mapped

    def compare(self,other):
        m,start,mapping = {},0,""
        if len(other) != len(self.word):
            return False
        for char in other:
            if char in "'.":
                mapping += char
            elif char in m:
                mapping += m[char]
            else:
                m[char] = str(start)
                mapping += str(start)
                start += 1
            l = len(mapping) - 1
            if self.mapped[:l] != mapping:
                return False
        return True

    def match(self,words):
        for word in words:
            if self.compare(word):
                self.matches.add(word)
        return self.matches
