class Solution(object):
    def titleToNumber(self, s):
        column = 0
        for i, l in enumerate(reversed(s)):
            column += (ord(l) - 64) * 26 ** i
        return column
