class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums)==0:
            return None
        newMin=nums[0]
        if len(nums)==1:
            return newMin
        for i in range(len(nums)-1):
            if nums[i+1] < nums[i] :
                if nums[i+1]<newMin:
                    newMin=nums[i+1]
        return newMin
