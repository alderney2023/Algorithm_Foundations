###########################################################################
# 求完全二叉树的节点个数
#

# 测试链接 : https://leetcode.cn/problems/count-complete-tree-nodes/
###########################################################################




class Solution:
    def countNodes(self, root) -> int:
        if not root:
            return 0
        height = self.mostLeft(root, 1)
        return self.f(root, 1, height)

    def f(self, cur, level, height):
        if level == height:
            return 1
        if self.mostLeft(cur.right, level+1) == height:
            return (1 << (height-level)) + self.f(cur.right, level+1, height)
        else:
            return self.f(cur.left, level+1, height) + (1 << (height-level-1))
        
    # 当前节点cur，它在level层, 返回从cur开始不停往左，能扎到几层
    def mostLeft(self, cur, level):
        while cur:
            level += 1
            cur = cur.left
        return level - 1

#---------------------------------------------------------------------------------   

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def main():
    node1 = TreeNode(1)
    node2 = TreeNode(2)
    node3 = TreeNode(3)
    node4 = TreeNode(4)
    node5 = TreeNode(5)
    node6 = TreeNode(6)
    node1.left, node1.right = node2, node3
    node2.left, node2.right = node4, node5
    node3.left = node6
    print(Solution().countNodes(node1)) 


if __name__ == "__main__":
    main()