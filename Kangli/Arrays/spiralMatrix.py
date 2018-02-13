class Solution(object):
    def spiralOrder(self, matrix):
        if not matrix or not matrix[0]:
            return []
        res = []
        colBegin, colEnd, rowBegin, rowEnd = 0, len(matrix[0])-1, 0, len(matrix)-1

        while colBegin <= colEnd and rowBegin <= rowEnd:
            for i in range(colBegin, colEnd+1):
                res.append(matrix[rowBegin][i])
            rowBegin += 1

            for i in range(rowBegin, rowEnd+1):
                res.append(matrix[i][colEnd])
            colEnd -= 1
            if rowBegin <= rowEnd:
                for i in range(colEnd, colBegin-1, -1):
                    res.append(matrix[rowEnd][i])
            rowEnd -= 1 
            
            if colBegin <= colEnd:
                for i in range(rowEnd, rowBegin-1, -1):
                    res.append(matrix[i][colBegin])
            colBegin += 1 

        return res

                
            
        
