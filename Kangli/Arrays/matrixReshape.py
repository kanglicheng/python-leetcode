# 566
class Solution(object):
    def matrixReshape(self, nums, r, c):
        l, w = len(nums), len(nums[0])
        if r*c != l*w:
            return nums
        result = [[]]
        for i in range(l):
            for j in range(w):
                elt = nums[i][j]
                if len(result[-1]) < c:
                    result[-1].append(elt)
                else:
                    result.append([elt])
        return result
        
