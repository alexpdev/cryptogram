class InvalidChar(Exception):
    pass

class Map:

    def map_sequence(self,seq):
        lst = []
        for item,mapp in self.gen_map(seq):
            lst.append(mapp)
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
