# lc problem 9
# Determine whether an integer is a palindrome.

class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if (x<0 or ()):
            return False
        rev = 0
        while (x!=0):
            rev = rev*10 + x%10
            x = x/10
        return (x==rev or x==rev/10)
# what's wrong with the if condition?
