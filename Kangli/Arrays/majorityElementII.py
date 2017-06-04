class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        # make a set(nums) and count the occurence of each element in nums
        """
        if len(nums) ==0:
            return []
        result=[]
        oneThird= len(nums)/3
        for elt in set(nums):
            if nums.count(elt) > oneThird:
                result.append(elt)
                
        return result
