"""
Problem 4
10.0/10.0 points (graded)
Write a function is_triangular that meets the specification below. A triangular number is a number obtained by the continued summation of integers starting from 1. For example, 1, 1+2, 1+2+3, 1+2+3+4, etc., corresponding to 1, 3, 6, 10, etc., are triangular numbers.
"""

def is_triangular(k):
    n=1
    while ( k >0):
        k -= n
        n+=1
    return k ==0
