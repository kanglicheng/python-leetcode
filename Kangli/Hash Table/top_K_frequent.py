from collections import defaultdict
class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        d = defaultdict(int)
        res= []
        for n in nums: #fill a dictionary with counts of occurence of n in nums
            d[n] +=1 
        
        
        for w in sorted(d, key=d.get, reverse=True):
            res.append(w)
        
        return [ res[i] for i in range(k)]
