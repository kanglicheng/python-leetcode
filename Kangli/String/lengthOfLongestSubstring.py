class Solution:
    def lengthOfLongestSubstring(self, s):
        d, j, ans = {}, 0, 0
        for i, c in enumerate(s):
            if c in d and d[c] >= j:
                j = d[c] + 1 
            ans = max(ans, i-j+1)
            d[c] = i
        return ans 
 
