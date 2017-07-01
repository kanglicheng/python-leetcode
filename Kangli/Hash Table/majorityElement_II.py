"""
Given an integer array of size n, find all elements that appear more than ⌊ n/3 ⌋ times. 
The algorithm should run in linear time and in O(1) space.
"""
# Straightforward but O(n) space.
def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        if not nums:
            return []
        d= {}
        res=[]
        m = len(nums)/3
        for n in nums:
            d[n] = 1 if n not in d else d[n] +1
            
        for n in d:
            if d[n] >m:
                res.append(n)
        return res
