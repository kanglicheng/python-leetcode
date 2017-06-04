class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums: return 0
        if len(nums)==1: return 1
        i=0
        for j in range(1, len(nums)):
            if nums[i]!=nums[j]:
                nums[i+1]=nums[j]
                i+=1
        return i+1
