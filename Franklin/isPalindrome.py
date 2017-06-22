# lc problem 9
# Determine whether an integer is a palindrome.

class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if (x<0):
            return False

        rev = 0; y = x
        while (y!=0):
            rev = rev*10 + y%10
            y = y/10
        return (x==rev)
