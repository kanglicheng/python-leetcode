class Solution(object):
    def maximalSquare(self, matrix):
        if not matrix: 
            return 0
        m , n = len(matrix),len(matrix[0])
        dp = [[0 if matrix[i][j]=='0' else 1 for j in xrange(n)]for i in xrange(m)]
        for i in range(1, len(matrix)):
            for j in range(1, len(matrix[0])):
                if matrix[i][j] == '1':
                    dp[i][j] = 1 + int(min(dp[i-1][j-1], dp[i-1][j], dp[i][j-1]))
        maxEdge = max(max(row) for row in dp)
        return maxEdge**2 
    
