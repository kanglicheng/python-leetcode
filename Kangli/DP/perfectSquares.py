sample 3626 ms submission
class Solution(object):
    def numSquares(self, n)
        #這題用dp來做 dp[i]儲存數字i由幾個square number組成 dp[i]=min(dp[i-1*1],dp[i-2*2],...)+1
        dp=[0 for i in range(n+1)]
        for i in range(1,n+1):
            j=1
            minv=2147483647
            if math.sqrt(i)-int(math.sqrt(i))==0:
                dp[i]=1
                continue
            while i-j*j>=0:
                if minv>dp[i-j*j]:
                    minv=dp[i-j*j]
                j+=1
            dp[i]=minv+1
        return dp[n]
