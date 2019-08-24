class Solution(object):
    def findMaxAverage(self, nums, k):
        a = [0]*(len(nums))
        temp = 0
        for i in range(len(nums)):
            temp += nums[i]
            a[i] = temp
        a= [0] + a
        maxKSum = min(a)
        for i in range(k, len(nums)+1):
            maxKSum = max(maxKSum, a[i] - a[i-k])
        return maxKSum/k
