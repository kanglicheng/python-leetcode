class Solution(object):
    def minCostClimbingStairs(self, cost):
        cost = cost+[0]
        dp = [0]*(len(cost))
        dp[0], dp[1] = cost[0], cost[1]
        for i in range(2, len(dp)):
            dp[i] = cost[i] + min(dp[i-1], dp[i-2])
        return dp[-1]

# Using O(1) space
class Solution(object):
    def minCostClimbingStairs(self, cost):
        d1, d2, k = 0, 0, 0
        for i in range(2, len(cost)+1):
            k = min(d1 + cost[i-2], d2+ cost[i-1])
            d1, d2 = d2, k
        return k
