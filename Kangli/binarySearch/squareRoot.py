
#sample 72 ms submission
class Solution(object):
    def mySqrt(self, x):
        if x <1:
            return 0
        i = 1
        while i*i <= x:
            l = i
            i*=2
            r = i
        while l < r:
            mid = (l+r)/2
            if mid*mid == x:
                return mid
            elif mid*mid > x:
                r = mid-1
            else:
                l = mid+1
        if l*l > x:
            return l-1
        else:
            return l
        
