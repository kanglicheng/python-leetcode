class Solution(object):
    def minCostClimbingStairs(self, cost):
        cost = cost+[0]
        dp = [0]*(len(cost))
        dp[0], dp[1] = cost[0], cost[1]
        for i in range(2, len(dp)):
            dp[i] = cost[i] + min(dp[i-1], dp[i-2])
        return dp[-1]
