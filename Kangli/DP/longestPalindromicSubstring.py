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
