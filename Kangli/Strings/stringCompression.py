class Solution(object):
    def compress(self, chars):
        res = []
        count = 1
        for i in range(len(chars)-1):
            if chars[i] == chars[i+1]:
                count += 1
            else:
                res.append(chars[i])
                if count >1:
                    res.extend(list(str(count)))
                count = 1
        res.append(chars[-1])
        if count >1:
            res.extend(list(str(count)))        
        chars[:] = res
        return len(chars)
