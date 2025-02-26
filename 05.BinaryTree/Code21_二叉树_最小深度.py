###########################################################################
# 二叉树的最小深度
# 给定一个二叉树，找出其最小深度。
# 最小深度是从根节点到最近叶子节点的最短路径上的节点数量。
#
# https://leetcode.cn/problems/minimum-depth-of-binary-tree
###########################################################################

def minDepth(self, root: Optional[TreeNode]) -> int:
    if not root:
        return 0
    if not root.left and not root.right:
        return 1
        
    left = right = float('inf')
    if root.left:
        left = self.minDepth(root.left)
    if root.right:
        right = self.minDepth(root.right)
    return min(left, right) + 1