#clean dp solution
class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        max_len, res = 0, ""
        dp = [[False for x in range(len(s))] for y in range(len(s))]
        for i in range(len(s)-1, -1, -1):
            for j in range(i, len(s)):
                dp[i][j] = s[i] == s[j] and (j-i < 3 or dp[i+1][j-1])
                if dp[i][j] and j-i+1 > len(res):
                    res = s[i:j+1]
        return res
       
class Solution(object):
    def longestPalindrome(self, s):
        st = 0
        maxl = 0
        dp = [[False]*1000 for _ in range(1000)]
        for i in reversed(range(len(s))):
            for j in range(i,len(s)):
                if s[i] == s[j] and (i+1>j-1 or dp[i+1][j-1] ):
                    dp[i][j] = True
                    if j-i+1 > maxl:
                        st = i
                        maxl = j-i+1

        return s[st:st+maxl]
