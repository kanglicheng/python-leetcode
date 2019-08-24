# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def inorderTraversal(self, root):
        res = []
        self.inOrder(root, res)
        return res 
    
    def inOrder(self, root, res):
        if root:
            self.inOrder(root.left, res)
            res.append(root.val)
            self.inOrder(root.right, res)