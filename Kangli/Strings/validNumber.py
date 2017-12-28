class Solution(object):
    def isNumber(self, s):
        try:
            n = float(s)
        except ValueError:
            return False
        return True
        
