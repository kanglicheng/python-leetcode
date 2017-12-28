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
