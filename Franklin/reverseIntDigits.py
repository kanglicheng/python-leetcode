#lc problem 7
#Reverse digits of an integer (keep the negative sign).
#The input is assumed to be a 32-bit signed integer. Your function should return 0 when the reversed integer overflows.

class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        boo = 0
        if (x<0):
            boo = 1
            x = -x
        x_reversed_str = str(x)[::-1]
        x_reversed_int = int(x_reversed_str)
        if (boo==1):
            x_reversed_int = -x_reversed_int
        if (abs(x_reversed_int)>2**31 -1):
            return 0
        else:
            return x_reversed_int

        # This solution is not optimal. Try to think of another one.
