#first solution, O(N) time and space
class Solution(object):
    def numDecodings(self, s):
        if not s:
            return 0
        dp = [0]*(len(s)+1)
        dp[0] = 1 
        for i in range(1, len(s)+1):
            if s[i-1] != '0':
                dp[i] += dp[i-1]
            if i != 1:
                if int(s[i-2:i]) in range(10, 27):
                    dp[i] += dp[i-2]
        return dp[len(s)]

    
#O(N) time, O(1) space DP via "general fibonacci numbers"
class Solution(object):
    def numDecodings(self, s):
        if len(s) == 0 or s[0] == '0':
            return 0
        prev, prev_prev = 1, 0
        for i in xrange(len(s)):
            cur = 0
            if s[i] != '0':
                cur = prev
            if i > 0 and (s[i - 1] == '1' or (s[i - 1] == '2' and s[i] <= '6')):
                cur += prev_prev
            prev, prev_prev = cur, prev
        return prev
                
         
