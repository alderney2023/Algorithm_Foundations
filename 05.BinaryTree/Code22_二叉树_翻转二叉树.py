###########################################################################
# 翻转二叉树
#
# https://leetcode.cn/problems/invert-binary-tree
###########################################################################

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return 
        a = self.invertTree(root.left)
        b = self.invertTree(root.right)
        root.left, root.right = b, a
        return root        