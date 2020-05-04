# /usr/bin/python3
# ~*~ charset: utf8 ~*~
# Cryptogram: version 0.1.1
#############################################################################
##
## Copyright (C) 2020 ASPDEV.
##
## Cryptogram v0.1.1
## All rights reserved.
##
## You may use this file under the terms of the GNU AGPLv3 license:
##
## THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
## "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
## LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR
## A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT
## OWNER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL,
## SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT
## LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE,
## DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY
## THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
## (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
## OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE."
##
##
#############################################################################
class InvalidChar(Exception):
    pass

class PhraseMap:
    def __init__(self,phrase,key,window):
        self.phrase = phrase
        self.key = key
        self.window = window
        self.partials = self.phrase_split()

    def addKeys(self,part,word):
        chars = []
        for w,p in zip(word,part):
            if p not in self.key:
                self.key[p] = w
                chars.append(p)
                self.window.add_keys((p,w))
        return tuple(chars)

    def removeKeys(self,chars):
        for i in chars:
            self.window.remove_keys(i)
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
            elif word[i] in vals or char == word[i]:
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
