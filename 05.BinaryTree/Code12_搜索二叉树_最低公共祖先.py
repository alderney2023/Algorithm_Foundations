###########################################################################
#搜索二叉树上寻找两个节点的最近公共祖先
#
#测试链接: https://leetcode.cn/problems/lowest-common-ancestor-of-a-binary-search-tree/
###########################################################################


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if (not root) or (root.val > min(p.val, q.val) and root.val < max(p.val,q.val)) or \
            root.val == p.val or \
            root.val == q.val:
            return root
        if root.val < min(p.val, q.val):
            return self.lowestCommonAncestor(root.right , p, q)
        if root.val > max(p.val, q.val):
            return self.lowestCommonAncestor(root.left, p, q)
        

    def lowestCommonAncestor2(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':

        while root.val != p.val and root.val != q.val:
            if root.val > min(p.val, q.val) and root.val < max(p.val,q.val):
                break
            if root.val < min(p.val, q.val):
                root = root.right
            elif root.val > max(p.val, q.val):
                root = root.left
        return root