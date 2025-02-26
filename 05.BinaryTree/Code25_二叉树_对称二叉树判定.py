###########################################################################
# 对称二叉树
# 给你一个二叉树的根节点 root ， 检查它是否轴对称。
#
# https://leetcode.cn/problems/symmetric-tree
###########################################################################

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:

        def process(l,r):
            if not l and not r: 
                return True
            if not l or not r or l.val != r.val:
                return False
            return process(l.left, r.right) and process(l.right, r.left)

        if not root :
            return True
        return process(root.left, root.right)       