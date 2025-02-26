###########################################################################
# 二叉树的锯齿形层序遍历
# 给你二叉树的根节点 root ，返回其节点值的 锯齿形层序遍历 。
# （即先从左往右，再从右往左进行下一层遍历，以此类推，层与层之间交替进行）。
#
# https://leetcode.cn/problems/binary-tree-zigzag-level-order-traversal
###########################################################################

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root: 
            return []
        queue = [root]
        res = []
        subres= []
        curLevelEnd = root
        nextLevelEnd = None
        reverse = False
        while queue:
            cur = queue.pop(0)
            subres.append(cur.val)
            if cur.left:
                queue.append(cur.left)
                nextLevelEnd = cur.left
            if cur.right:
                queue.append(cur.right)
                nextLevelEnd = cur.right

            if cur == curLevelEnd:
                if reverse:
                    res.append(subres[::-1])
                else:
                    res.append(subres)
                reverse = not reverse
                subres = []
                if nextLevelEnd:
                    curLevelEnd = nextLevelEnd
        return res