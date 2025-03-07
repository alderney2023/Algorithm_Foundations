###########################################################################
# 修剪搜索二叉树
# 测试链接 : https://leetcode.cn/problems/trim-a-binary-search-tree/
###########################################################################


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def trimBST(self, root: Optional[TreeNode], low: int, high: int) -> Optional[TreeNode]:
        if not root:
            return None
        if root.val < low:
            root = self.trimBST(root.right ,low, high)
        elif root.val > high:
            root = self.trimBST(root.left , low, high)
        else:
            root.left = self.trimBST(root.left , low, high)
            root.right = self.trimBST(root.right ,low, high)

        return root