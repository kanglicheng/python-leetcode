# Generate all subsets that sum to target using elements from candidates. Each number in 
# candidates can be used an unlimited number of times
class Solution(object):
    def combinationSum(self, candidates, target):
        self.res = []
        
        def dfs(candidates, target, temp, index):
            if target == 0:
                self.res.append(temp[:])
                return 
            if target <0:
                return
            for i in range(index, len(candidates)):
                temp.append(candidates[i])
                dfs(candidates, (target - candidates[i]), temp, i)
                temp.pop()
        dfs(candidates, target, [], 0)
        return self.res
        
        
