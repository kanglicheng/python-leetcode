from operator import itemgetter
class Solution(object):
    def frequencySort(self, s):
        d, st = {}, ""
        for c in s:
            d[c] = 1 if c not in d else d[c] + 1
        arr = sorted(d.items(), key=itemgetter(1), reverse = True)    
        for pair in arr:
            st += pair[0]*pair[1]
        return st
