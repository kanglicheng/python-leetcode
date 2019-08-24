class Solution(object):
    def minDistance(self, word1, word2):
        l1= len(word1) + 1
        l2 = len(word2) + 1
        
        dp = [[0 for b in xrange(l2)] for c in xrange(l1)] #create two dimensional array for storing subproblem solutions
        for i in xrange(l1):
            dp[i][0] = i
        for j in xrange(l2):
            dp[0][j] = j
        for i in xrange(1, l1):
            for j in xrange(1, l2):
                dp[i][j] = min(dp[i-1][j]+1, dp[i][j-1]+1, dp[i-1][j-1]+(word1[i-1]!=word2[j-1]))
        return dp[-1][-1]
                    
#sample 282 ms submission
class Solution(object):
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        m = len(word1)
        n = len(word2)
        dp = [[0 for x in xrange(n+1)] for x in xrange(m+1)]
        
        for i in xrange(m+1):
            for j in xrange(n+1):
                if i == 0:
                    dp[i][j] = j
                elif j == 0:
                    dp[i][j] = i
                elif word1[i-1] == word2[j-1]:
                    dp[i][j] = dp[i-1][j-1]
                else:
                    dp[i][j] = 1 + min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1])
        
        return dp[m][n]
            
