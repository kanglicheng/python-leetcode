# very slow, only beats 5% of submissions!
class Solution(object):
    def uniquePaths(self, m, n):
        a= [[1 for i in range(n)] for _ in range(m)]
        for i in range(1, m):
            for j in range(1, n):
                a[i][j] = a[i-1][j] + a[i][j-1]
        return a[-1][-1]
