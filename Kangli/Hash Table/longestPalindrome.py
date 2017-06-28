"""
Given a string which consists of lowercase or uppercase letters, find the length of the longest palindromes that can be built with those letters.

This is case sensitive, for example "Aa" is not considered a palindrome here.

Note:
Assume the length of given string will not exceed 1,010.

Explanation:
Key observation about palindromes. They must contain an even number of each unique letter except possibly a single odd letter
in the middle of the string.

Use a dictionary to keep track of what can be used in the palindrome.
Populate the dictionary and keep track of the length by the following method. If a letter k has been seen before, 
it can be used in the palindrome. Reset the value of k back to zero, because the palindrome will use the two copies of k and
the length of the palindrome increases by 2. Finally, look for any single letter in the dictionary with non-zero value
and add 1 to the length if found.
"""

class Solution(object):
    def longestPalindrome(self, s):
        d = {}
        length = 0
        for i in s:
            if d.get(i):
                d[i] = 0
                length += 2
            else:
                d[i] = 1
        for j in d:
            if d[j] != 0:
                length += 1
                break
        return sum
