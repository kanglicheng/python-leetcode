#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul 28 13:28:37 2017

@author: Steven
"""
"""
def max_val(t):

    ans =0
    for c in t:
        if type(c) == int and c >ans:
            ans =c
        else:
            max_val(c)

    return ans

print (max_val((5, [1, 9]) ))
"""

def max_val(t):
    ans =0
    _max_val(t, ans)

def _max_val(t, ans):
    for c in t:
        if type(c) != int:
            max_val(c)
        elif c > ans:
            ans =c
    if type(ans) == int:
        return ans
    else:
        return max(ans)

print ( max_val(((2, 3, 4), (5, 6), [10, [11]])))


#print (max_val(([[2, 1, 5], [4, 2], 6], ([2, 1], (7, 7, 5), 6))))
