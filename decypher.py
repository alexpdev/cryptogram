from ranks import ranks
from phrases import Phrases

def decypher(phrase,ranks):
    first = get_sort(ranks)

def get_sort(ranks):
    first = []
    r = ranks.copy()
    l = len(r)
    z = 0
    for k,v in sorted(ranks.items(),key=lambda x:x[1],reversed=True):
        if z < 7:
            first.append(k)
            z += 1
    return first







if __name__ == "__main__":
    for phrase in Phrases:
        decypher(phrase,ranks)
