# lc problem 69
# Compute and return the square root of x.

class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        #corner case
        if (x==1):
            return 1
        low = 0
        high = x
        mid = (low+high)/2
        while (low!=high-1):
            if (mid**2 < x):
                low = mid
            elif (mid**2 == x):
                return mid
            elif (mid**2 >x):
                high = mid
            mid = (low+high)/2
        return mid

    # This solution uses binary search, and I am thinking if Newton's method would work?
