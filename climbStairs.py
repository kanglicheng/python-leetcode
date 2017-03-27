#recursive top-down solution with memoization 
class Solution(object):
  memo=[]
  def climbStairs(self, n):
    global memo
    memo=[None]*(n+1)
    
    return self._climbStairs(n)
    
  def _climbStairs(self, n):
      if(n==0):
        return 0
      if(n == 1):
          return 1
      elif(n==2):
          return 2
      if(memo[n] is not None):
        return memo[n]
      memo[n]=self._climbStairs(n-1)+self._climbStairs(n-2)
      return memo[n]
     
    #bottom up iterative 
""" def climbStairs(n)
     nw=None*(n+1)
     nw[0]=1
     nw[1]=2
     i=3
     while i<= n: 
        nw[i]=nw[i-1]+nw[i-2]
        i+=1
    return nw[n]
 climbStairs(5)
""" 
    
    
    