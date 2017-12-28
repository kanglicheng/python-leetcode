# Generate all permutations of an array that may have duplicate elements,
# but without any duplicate subsets. Not the same as generate all combinations. 
class Solution(object):
    def permuteUnique(self, nums):
        self.res = []
        self.visited = [False] * len(nums)
        self.permuteHelper(sorted(nums), [])
        return self.res
        
    def permuteHelper(self, nums, temp):
        if len(nums) == len(temp):
            self.res.append(temp[:])
        for i in range(len(nums)):
            if self.visited[i]:
                continue
            if i > 0 and nums[i] == nums[i-1] and self.visited[i-1]: continue
            else:
                self.visited[i] = True
                temp.append(nums[i])
                self.permuteHelper(nums, temp)
                self.visited[i] = False
                temp.pop()
        
    
