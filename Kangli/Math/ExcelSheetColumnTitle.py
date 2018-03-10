class Solution(object):
    def convertToTitle(self, n):
        charList = list('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
        res = ''
        while n > 0:
            res += charList[(n-1) % 26]
            n = (n-1) / 26  # let 26 become Z not AZ
        return res[::-1]

#sample 25 ms submission
class Solution(object):
    def convertToTitle(self, n):
        """
        :type n: int
        :rtype: str
        """
        res = ''
        while n:
            remainder = n % 26
            n /= 26
            if remainder == 0:
                res = 'Z' + res
                n -= 1
            else:
                res = chr(ord('A') + remainder - 1) + res
        return res
