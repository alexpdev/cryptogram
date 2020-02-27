class Manager:

    def __init__(self,phrase):
        self.amount = 0
        self.phrase = phrase
        self.id = 0
        self.track = {}
        self.end = False
        self.total_chars = self.total()

    def log(self,key):
        keylen = len(key)
        if keylen in self.track:
            self.track[keylen][self.id] = key
            self.id += 1
        else:
            self.track[keylen] = {self.id:key}
            self.id += 1
        if keylen >= self.amount:
            self.amount = keylen
            if self.amount > self.total_chars/2:
                self.swap(key)
            self.checkisfull(keylen)
        return self.end

    def checkisfull(self,keylen):
        if keylen >= self.total_chars:
            s = input("Continue? (y/n):  ")
            if s == "n":
                self.end = True
        return

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
        for i in self.phrase:
            if i.isalpha() and i not in chars:
                chars.append(i)
        return len(chars)
