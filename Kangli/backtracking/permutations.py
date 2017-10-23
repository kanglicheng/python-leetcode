#10/17/17 Tuesday
#Given a collection of distinct numbers, return all possible permutations.
#recursive solution
class Solution(object):
    def permute(self, nums):
        res = []
        self.permuteHelper( nums, 0, res)
        return res
    def permuteHelper(self, nums, start, results):
                if start >= len(nums):
                    results.append(nums[:])
                else:
                    for i in range(start, len(nums)):
                        nums[i], nums[start] = nums[start], nums[i]
                        self.permuteHelper( nums, start +1, results)
                        nums[start], nums[i] = nums[i], nums[start]

s = Solution()
arr = [1, 2, 3]
print s.permute(arr)