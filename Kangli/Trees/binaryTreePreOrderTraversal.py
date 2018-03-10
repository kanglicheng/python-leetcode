# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):   
    def preorderTraversal(self, root):
        res = []
        self.preOrder(root, res)
        return res

    def preOrder(self, root, res):
        if root:
            res.append(root.val)
            self.preOrder(root.left, res)
            self.preOrder(root.right, res)
