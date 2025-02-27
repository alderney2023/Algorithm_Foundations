###########################################################################
# 收集累加和等于aim的所有路径
# 测试链接 : https://leetcode.cn/problems/path-sum-ii/
###########################################################################


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        if not root:
            return []
        res = []
        path = []
        self.process(targetSum, root, 0, path, res)
        return res
        
    def process(self, targetSum, node, sum, path, res):
        
        path.append(node.val)
        sum += node.val
        if (not node.left) and (not node.right) and sum == targetSum:
            path_copy = path.copy()
            res.append(path_copy)
        else:
            if node.left:
                self.process(targetSum, node.left, sum, path, res)
            if node.right:
                self.process(targetSum, node.right, sum, path, res)
        sum -= node.val
        path.pop()