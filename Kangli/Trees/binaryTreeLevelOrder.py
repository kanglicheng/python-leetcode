class Solution():
    def levelOrder(self, root):
        ret = []
        level = [root] 
        while root and level:
            currentNodes = []
            nextLevel = []
            for node in level:
                currentNodes.append(node.val)
                if node.left:
                    nextLevel.append(node.left)
                if node.right:
                    nextLevel.append(node.right)
            ret.append(currentNodes)
            level = nextLevel      
        return ret


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []
        queue, result = [root], [[root.val]]
        
        while queue:
            queue_new = queue
            queue = []
            result_temp = []
            for current in queue_new:
                # current = queue_new.pop()
                if current.left:
                    queue.append(current.left)
                    result_temp.append(current.left.val)
                if current.right:
                    queue.append(current.right)
                    result_temp.append(current.right.val)
            if len(result_temp)>0:
                result.append(result_temp)
                
        return result
