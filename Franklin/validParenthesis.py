#lc problem 20
#Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
#The brackets must close in the correct order, "()" and "()[]{}" are all valid but "(]" and "([)]" are not.

class Solution(object):
    #solution using stack
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        mid = len(s)/2 - 1
        boo = (len(s)%2 == 0)
        map = {'(':')', '[':']', '{':'}'}
        stack = []
        
        for c in s:
            if c in map.keys():
                stack.append(c)
            elif c in map.values():
                if stack ==[] or c != map[stack.pop()]:
                    return False
        return (stack == [])
