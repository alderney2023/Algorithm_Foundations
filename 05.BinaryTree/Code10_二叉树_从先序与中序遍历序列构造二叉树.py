###########################################################################
# 从前序与中序遍历序列构造二叉树
# 给定两个整数数组 preorder 和 inorder ，
#   其中 preorder 是二叉树的先序遍历， inorder 是同一棵树的中序遍历，请构造二叉树并返回其根节点。
#
#
# https://leetcode.cn/problems/construct-binary-tree-from-preorder-and-inorder-traversal
###########################################################################



class Solution:
    def buildTree(self, preorder, inorder):
        if len(preorder) == 0:
            return None

        inorder_dic = {}
        for i in range(len(inorder)):
            inorder_dic[inorder[i]] = i

        root = TreeNode(preorder[0])
        root_pos =  inorder_dic[preorder[0]]
        left_inorder = inorder[0:root_pos]
        left_len = root_pos
        right_inorder = inorder[(root_pos+1):]
        left_preorder = preorder[1:(1+left_len)]
        right_preorder = preorder[(1+left_len):]
        root.left = self.buildTree(left_preorder, left_inorder)
        root.right = self.buildTree(right_preorder, right_inorder)

        return root

#---------------------------------------------------------------------------------   

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def main():
    node3 = TreeNode(3)
    node9 = TreeNode(9)
    node20 = TreeNode(20)
    node15 = TreeNode(15)
    node7 = TreeNode(7)
    node3.left, node3.right = node9, node20
    node20.left, node20.right = node15, node7
    print(levelOrder1(node3)) 
    print(levelOrder2(node3)) 
    print(levelOrder3(node3)) 

if __name__ == "__main__":
    main()