'''
Given a collection of intervals, merge all overlapping intervals.

For example,
Given [1,3],[2,6],[8,10],[15,18],
return [1,6],[8,10],[15,18].
'''

# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution(object):
    def merge(self, intervals):
        result = []
        for i in sorted(intervals, key=lambda i: i.start): #sort each array by 
            if result and i.start <= result[-1].end: #not empty and interval i's start <= last added interval's end
                result[-1].end = max(result[-1].end, i.end) #set the end to max of previous end and new i's end
            else:
                result.append(i) #otherwise add the interval
        return result
