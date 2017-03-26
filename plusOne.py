#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 25 23:10:37 2017

@author: Steven
"""

class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        result=0
        n=len(digits)-1
        for i in digits:
           result+= i*10**n
           n-=1
        result+=1
        print(result)
        return [int(i) for i in str(result)] #convert back to array
        
def main():
    digits=[0]
    test2=[2, 3, 7]
    s=Solution()
    s.plusOne(digits)
    s.plusOne(test2)
main()