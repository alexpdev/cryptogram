class UpdateKey(Exception):
    pass

class Solved(Exception):
    pass

class EndDecrypt(Exception):
    pass

class BaseManager:
    def __init__(self,**kwargs):
        self._phrase = kwargs["phrase"]
        self.args = kwargs
        self.id = 0
        self.last = 0
        self.amount = 0
        self.track = {}
        self.frequency = None
        self._total = None

    def log(self,key):
        keyLen = len(key)
        self.track[self.id] = key
        self.id += 1
        if keyLen > self.amount:
            self.amount = keyLen
            self.review(key,keyLen)
        return

    def review(self,key=None,keylen=None):
        return self._review_status(key,keylen)

    def _review_status(self,key,keylen):
        self.swap(key)

    def swap(self,key):
        phrase = ""
        for i in self._phrase:
            if i in key:
                phrase += key[i]
            else:
                phrase += i
        print(phrase)

    @property
    def total(self):
        if not self._total:
            chars = []
            for char in self._phrase:
                if char.isalpha() and char not in chars:
                    chars.append(char)
            self._total = len(chars)
            self.frequency = int(self._total * .70)
        return self._total


class TerminalManagerMixin():

    def getInput(self,key):
        for k,v in key.items():
            print("Old: ",k," New: ",v)
        print("Which should be permanently replaced")
        chars = input("Enter each letter to keep or Enter 1 for all:\n")
        new_keys = {}
        if chars == "1":
            for k,v in key.items():
                new_keys[k] = v
        else:
            for char in chars:
                new_keys[char] = key[char]
        self.args["key"] = new_keys
        return

    def update_input(self):
        inp = input("REFRESH KNOWN KEYS? [(y)es,(n)o,(i)ncrease,(e)nd]:")
        if inp == "e":
            print("ENDING DECRYPTION")
            raise EndDecrypt
        if inp == "i":
            self.frequency += 1
            print("Frequency",self.frequency,"Total",self.total)
            return False
        if inp != "y":
            return False
        else:
            return True



class TermManager(BaseManager,TerminalManagerMixin):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)

    def review(self,key,keyLen):
        if keyLen == self.total:
            print("SOLVED!!!")
            raise Solved
        elif keyLen >= (self.total*.75) and keyLen >= self.frequency:
            self.swap(key)
            if self.update_input():
                self.getInput(key)
                raise UpdateKey
        if self.id - self.last >= 500:
            self.swap(key)
            print(self.id)
