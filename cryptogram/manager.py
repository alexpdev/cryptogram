class ResetKey(Exception):
    pass

class Solved(Exception):
    pass

class Manager:
    def __init__(self,**kwargs):
        self.phrase = kwargs["phrase"]
        self.verbosity = kwargs["verbosity"]
        self.output = kwargs["output"]
        self.args = kwargs
        self.id = 0
        self.amount = 0
        self.track = {}
        self.end = False
        self.total_chars = self.total()

    def log(self,key):
        keylen = len(key)
        self.track[self.id] = key
        self.id += 1
        return self.review_status(keylen,key)

    def review_status(self,keylen,key):
        if keylen > self.amount:
            print(self.swap(key))
            if not self.checkfilled(keylen):
                chars = self.getInput(key)
            else:
                self.amount = keylen
        return self.end

    def checkfilled(self,keylen):
        klen = self.total_chars//2
        if keylen >= klen:
            s = input("Continue? (y/n):  ")
            if s == "n":
                raise Solved
        return False

    def swap(self,key):
        phrase = ""
        for i in self.phrase:
            if i in key:
                phrase += key[i]
            else:
                phrase += i
        print(phrase)

    def total(self):
        chars = []
        for char in self.phrase:
            if char.isalpha() and char not in chars:
                chars.append(char)
        return len(chars)

    def getInput(self,key):
        inp = input("Refresh Keys? (y/n)")
        if inp != "y":
            return
        for k,v in key.items():
            print("Old: ",k," New: ",v)
        print("Which should be permanently replaced")
        chars = input()
        for char in chars:
            self.args["key"][char] = key[char]
        return chars
