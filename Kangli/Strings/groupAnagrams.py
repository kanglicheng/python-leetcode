class Solution(object):
    def groupAnagrams(self, strs):
        d = collections.defaultdict(list)
        for s in strs:
            d["".join(sorted(s))].append(s)
        return [ group for group in d.values() ]
                    
# use a hash, sort each string and use it as a key. Append unsorted string to list of values. 
# return all values
