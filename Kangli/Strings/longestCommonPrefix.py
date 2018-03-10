class Solution(object):
    def longestCommonPrefix(self, strs):
        if not strs:
            return ""
        pref = strs[0]
        for i in range(1, len(strs)):
            while pref != strs[i][:len(pref)]:
                pref = pref[:-1]
        return pref
        
