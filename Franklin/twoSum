#lc problem 1
#Given an array of integers, return indices of the two numbers such that they add up to a specific target.

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        array = sorted(nums)
        i = 0
        j = len(array)-1
        
        while (array[i]+array[j] != target):
            if (array[i]+array[j] < target):
                i += 1
            else:
                j -= 1
        
        t0 = array[i]
        t1 = array[j]
        
        pos0 = nums.index(t0)
        pos1 = nums.index(t1)
        if (pos0 == pos1):
            pos1 = nums[pos0+1:].index(t1)
            pos1 += pos0+1
        return pos0,pos1
