class Solution(object):
    def findKthLargest(self, nums, k):
        j = len(nums)-1
        t = 1
        nums.sort()
        while j >= 0:
            if t ==k:
                return nums[j]
            else:
                j -= 1
                t +=1 
