class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        d = {}
        for i, n in enumerate(nums):
            if n not in d:
                d[n]=i
            else:
                if abs(i - d[n]) <= k:
                    return True
                else:
                    d[n]= i
        else:
            return False

# Basically the same solution
class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        d = {}
        for i, v in enumerate(nums):
            if v in d and i - d[v] <= k:
                return True
            d[v] = i
        return False
