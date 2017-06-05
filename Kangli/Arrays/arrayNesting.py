class Solution(object):
    def arrayNesting(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dic = {}
        result = -float('inf')
        for index in range(len(nums)):
        
            count = 1
            dic[index] = 1
            while True:
                if nums[index] not in dic:
                    count += 1
                    dic[nums[index]] = 1
                    index = nums[index]
                else:
                    result = max(result,count)
                    break
        return result
