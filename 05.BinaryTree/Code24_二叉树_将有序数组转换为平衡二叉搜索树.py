###########################################################################
# 将有序数组转换为二叉搜索树
# 给你一个整数数组 nums ，其中元素已经按 升序 排列，请你将其转换为一棵 平衡 二叉搜索树。
#
# https://leetcode.cn/problems/convert-sorted-array-to-binary-search-tree
###########################################################################

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        return self.process(nums,0, len(nums)-1)

    def process(self, nums,start, end):
        if start > end:
            return None
        mid = (start + end) >> 1
        root = TreeNode(nums[mid])
        root.left = self.process(nums,start, mid-1)
        root.right = self.process(nums, mid+1, end)
        return root
        