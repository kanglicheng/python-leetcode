sample 355 ms submission
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution(object):
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        # 若是len(preorder)為0 則返回空
        # 首次輸入邊界條件
        if len(preorder) == 0:
            return None
        # 遞歸edge
        # 若是長度為1 則返回當前值
        if len(preorder) == 1:
            return TreeNode(preorder[0])
        root = TreeNode(preorder[0])
        # 從preorder的第一個找出 inorder的index
        index = inorder.index(root.val)
        
        # 記得切片不包括尾數 左閉右開 -> [1:0]==[]
        root.left = self.buildTree(preorder[1:index+1], inorder[0:index])
        root.right = self.buildTree(preorder[index+1:], inorder[index+1:])
        return root
