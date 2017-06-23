class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        if not nums1 or not nums2:
            return []
        d1={}
        res=[]
        
        for n in nums1:
            d1[n] =1 if n not in d1 else d1[n] +1
        
        for m in nums2:
            if d1.get(m)>0:
                res.append(m)
                d1[m] -=1
                
        return res
