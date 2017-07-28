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
    results=[]
    _max_val(t, ans, results)
    return max(results)


def _max_val(t, ans, results):
    for c in t:
        if type(c) != int:
            _max_val(c, ans, results)
        elif c > ans:
            ans =c
    results.append(ans)


print ( max_val(((2, 3, 4), (5, 6), [10, [11]])))

# Question 5
"""
def cipher(map_from, map_to, code):
     map_from, map_to: strings where each contain
                          N unique lowercase letters.
        code: string (assume it only contains letters also in map_from)
        Returns a tuple of (key_code, decoded).
        key_code is a dictionary with N keys mapping str to str where
        each key is a letter in map_from at index i and the corresponding
        value is the letter in map_to at index i.
        decoded is a string that contains the decoded version
        of code using the key_code mapping.
    # Your code here
"""
def cipher(map_from, map_to, code):
    d ={}
    ans =""
    for i, c in enumerate(map_from):
        d[c]= map_to[i]

    for c in code:
        ans += d[c]
    return (d, ans)

#print (max_val(([[2, 1, 5], [4, 2], 6], ([2, 1], (7, 7, 5), 6))))
