class Solution(object):
    def threeSumClosest(self, nums, target):
        nums.sort()
        res, ans = [], nums[0]+nums[1]+nums[2]
        for i in range(len(nums)):
            l, r = i+1, len(nums)-1
            while l < r:
                s = nums[i] + nums[l] + nums[r]
                if abs(target-s) < abs(target-ans):
                    while abs(target-s) < abs(target-ans):
                        ans = s
                        if ans > target:
                            r -= 1
                        else:
                            l += 1
                else:
                    if s > target:
                        r -= 1
                    else:
                        l+=1 
        return ans
