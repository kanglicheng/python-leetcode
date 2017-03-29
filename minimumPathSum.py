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
