class Solution(object):
    def merge(self, nums1, m, nums2, n):
        aIndex, bIndex, mergeIndex = m-1, n-1, m + n - 1
        while aIndex >= 0 and bIndex >= 0:
            if nums1[aIndex] > nums2[bIndex]:
                nums1[mergeIndex] = nums1[aIndex]
                aIndex -= 1
            else:
                nums1[mergeIndex] = nums2[bIndex]
                bIndex -= 1
            mergeIndex -= 1
        while bIndex >= 0:
            nums1[mergeIndex] = nums2[bIndex]
            bIndex -= 1
            mergeIndex -= 1
        
# learned it here https://www.youtube.com/watch?v=rZ9lcXCWSUg, https://www.byte-by-byte.com/mergearrays/
            
        
