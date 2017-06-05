#lc problem 13
#Given a roman numeral, convert it to an integer.
#Input is guaranteed to be within the range from 1 to 3999.

class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        i = 0
        result = 0
        length = len(s)
        map = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
        while (i<length):
            num1 = map[s[i]]
            #s[i] still has next numeral
            if (i+1 < length):
                num2 = map[s[i+1]]
                #two cases
                if (num1 >= num2):
                    result += num1
                    i += 1
                else:
                    result = result - num1 + num2
                    i += 2
            else: #s[i] is the last numeral
                result += num1
                # to jump out of loop
                i += 1
            
        return result
