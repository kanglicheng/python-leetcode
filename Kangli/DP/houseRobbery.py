class Solution(object):
    def rob(self, nums):
        if not nums:
            return 0
        elif len(nums) == 1:
            return nums[0]
        elif len(nums) == 2:
            return max(nums)
        dp = [0]*(len(nums))
        dp[0], dp[1] = nums[0], max(nums[1], nums[0])
        for i in range(2, len(nums)):
            dp[i] = max(nums[i] + dp[i-2], dp[i-1])
        return dp[-1]
