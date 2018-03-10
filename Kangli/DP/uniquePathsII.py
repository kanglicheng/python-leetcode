class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        if not obstacleGrid:
            return 0
        if obstacleGrid[0][0] == 1:
            return 0
        r, c = len(obstacleGrid), len(obstacleGrid[0])
        dp = [[0 for i in range(c)] for _ in range(r)]
        for i in range(r):
            if obstacleGrid[i][0] == 1:
                break
            dp[i][0] = 1 if obstacleGrid[i][0] == 0 else 0
        for j in range(c):
            if obstacleGrid[0][j] == 1:
                break
            dp[0][j] = 1 if obstacleGrid[0][j] == 0 else 0
        for i in range(1, r):
            for j in range(1, c):
                if obstacleGrid[i][j] == 1:
                    dp[i][j] = 0
                else:
                    dp[i][j] = dp[i-1][j] + dp[i][j-1]
        return dp[-1][-1]
        
