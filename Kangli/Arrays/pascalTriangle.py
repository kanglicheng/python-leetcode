# not very elegant, but accepted. Created Pascal's directly from definition
class Solution(object):
    def generate(self, numRows):
        ans = [[1], [1, 1]]
        if numRows == 0:
            return []
        elif numRows == 1:
            return [[1]]
        elif numRows == 2:
            return [[1], [1, 1]]
        else:
            for i in range(3, numRows +1):
                temp = [1]*i
                for j in range(i):
                    if j ==0 or j == i-1:
                        continue
                    else:
                        temp[j] = ans[i-2][j-1] + ans[i-2][j]
                ans.append(temp)
            return ans
        
def generate(self, numRows):
        res = [[1]]
        for i in range(1, numRows):
            res += [map(lambda x, y: x+y, res[-1] + [0], [0] + res[-1])]
        return res[:numRows]
