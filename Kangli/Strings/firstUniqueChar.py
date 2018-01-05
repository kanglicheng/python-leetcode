class Solution(object):
    def firstUniqChar(self, s):
        d={}
        for c in s:
            d[c] = 1 if c not in d else d[c] +1 
        for i, c in enumerate(s):
            if d[c] == 1:
                return i
        return -1

#build a hash of letter counts, then iterate through s and check count, return index of first letter with count = 1.
