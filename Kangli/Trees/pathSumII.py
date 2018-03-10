class Solution(object):
    def pathSum(self, root, sum):
        result = []
        self.dfs(root, sum, [], result)
        return result
    
    def dfs(self, node, sum, path, res):
        if not node:
            return
        if not node.left and not node.right:
            if node.val == sum:
                res.append(path + [node.val])
        self.dfs(node.left, sum - node.val, path + [node.val], res)
        self.dfs(node.right, sum - node.val, path + [node.val], res)
