class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m = len(grid) #get the dimensions 
        n = len(grid[0])
        for i in range(1, n):   #populate the first row of the grid with consecutive sums across
            grid[0][i] += grid[0][i-1]
        for i in range(1, m):   #replacing the first column of the grid with consecutive sums
            grid[i][0] += grid[i-1][0]
        for i in range(1, m):   #fill in the rest of the grid with the minimum sum to reach it.
            for j in range(1, n):
                grid[i][j] += min(grid[i-1][j], grid[i][j-1])
        return grid[-1][-1] #the top left element contains the solution

# 1/18/18 redo
class Solution(object):
    def minPathSum(self, grid):
        if len(grid) == 1 and len(grid[0]) == 1:
            return grid[0][0]
        r, c = len(grid), len(grid[0])
        dp = [[0 for i in range(c)] for _ in range(r)]
        dp[0][0] = grid[0][0]
        for i in range(c):
            dp[0][i] = grid[0][i] + dp[0][i-1]
        for j in range(r):
            dp[j][0] = grid[j][0] + dp[j-1][0]
        
        for i in range(1, r):
            for j in range(1, c):
                dp[i][j] = min(dp[i-1][j], dp[i][j-1]) + grid[i][j]
        return dp[-1][-1]
        
    
# sample 69 ms submission, cleaner than mine!
class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m, n = len(grid), len(grid[0])
        for i in range(m):
            for j in range(n):
                if i == 0 and j == 0:
                    continue
                elif i == 0:
                    grid[i][j] += grid[i][j-1]
                elif j == 0:
                    grid[i][j] += grid[i-1][j]
                else:
                    grid[i][j] += min(grid[i][j-1], grid[i-1][j])
        return grid[-1][-1]
    
    
    
    
