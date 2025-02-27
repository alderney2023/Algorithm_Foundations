###########################################################################
# 二叉树打家劫舍问题
# 小偷又发现了一个新的可行窃的地区。这个地区只有一个入口，我们称之为 root 。
# 除了 root 之外，每栋房子有且只有一个“父“房子与之相连。一番侦察之后，聪明的小偷意识到“这个地方的所有房屋的排列类似于一棵二叉树”。 
# 如果 两个直接相连的房子在同一天晚上被打劫 ，房屋将自动报警。
# 给定二叉树的 root 。返回 在不触动警报的情况下 ，小偷能够盗取的最高金额 。
#
# 测试链接 : https://leetcode.cn/problems/house-robber-iii/
###########################################################################

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    class info:
        def __init__(self,yes,no):
            self.yes = yes
            self.no = no

    def rob(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        info = self.process(root)
        return max(info.yes, info.no)
    
    def process(self,node):
        if not node:
            return self.info(0, 0)

        leftInfo = self.process(node.left)
        rightInfo = self.process(node.right)

        yes = node.val + leftInfo.no + rightInfo.no
        no = max(leftInfo.yes, leftInfo.no) + max(rightInfo.yes,rightInfo.no)

        return self.info(yes,no)