###########################################################################
# 二叉树最大特殊宽度
# 给你一棵二叉树的根节点 root ，返回树的 最大宽度 。
# 树的 最大宽度 是所有层中最大的 宽度 。
# 每一层的 宽度 被定义为该层最左和最右的非空节点（即，两个端点）之间的长度。
#   将这个二叉树视作与满二叉树结构相同，两端点间会出现一些延伸到这一层的 null 节点，这些 null 节点也计入长度。
# 题目数据保证答案将会在  32 位 带符号整数范围内。
#
# https://leetcode.cn/problems/maximum-width-of-binary-tree
###########################################################################


# 方法一： 借用字典和几个变量， leetcode 4s
class Solution:
    def widthOfBinaryTree(self, root) -> int:
        if not root:
            return 0
        queue = [root]
        dic = {}
        dic[root] = [1,1]
        curLevelEnd = root
        curLevelStart = root
        nextLevelEnd = None
        curLevel = 1
        maxWidth = 0
        while queue:
            curNode = queue.pop(0)
            nodeLevel, nodePosition = dic[curNode]

            if curLevel != nodeLevel:
                maxWidth = max(maxWidth, dic[curLevelEnd][1] - dic[curLevelStart][1] + 1)
                curLevelStart = curNode
                curLevelEnd = nextLevelEnd
                curLevel += 1

            if curNode.left:
                queue.append(curNode.left)
                dic[curNode.left] = [nodeLevel+1, nodePosition*2]
                nextLevelEnd = curNode.left
            if curNode.right:
                queue.append(curNode.right)
                dic[curNode.right] = [nodeLevel+1, nodePosition*2+1]
                nextLevelEnd = curNode.right

        maxWidth = max(maxWidth, dic[curLevelEnd][1] - dic[curLevelStart][1] + 1)

        return maxWidth
    
    #方法二： 写法更简单，但时间长些 leetcode 7s
    def widthOfBinaryTree2(self, root) -> int:
        if not root:
            return 0
        queue = [(root,0)]
        maxWidth = 0
  
        while queue:
            maxWidth = max(maxWidth, queue[-1][1] - queue[0][1] + 1)
            for i in range(len(queue)):
                curNode,pos = queue.pop(0)
                if curNode.left:
                    queue.append((curNode.left, pos*2))
                if curNode.right:
                    queue.append((curNode.right, pos*2+1))

        return maxWidth

#---------------------------------------------------------------------------------

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def main():
    # node1 = TreeNode(1)
    # node3 = TreeNode(3)
    # node2 = TreeNode(2)
    # node5 = TreeNode(5)
    # node30 = TreeNode(3)
    # node9 = TreeNode(9)
    # node1.left, node1.right = node3, node2
    # node3.left, node3.right = node5, node30
    # node2.right = node9

    node1 = TreeNode(1)
    node3 = TreeNode(3)
    node2 = TreeNode(2)
    node5 = TreeNode(5)
    node1.left, node1.right = node3, node2
    node3.left = node5

    print(Solution().widthOfBinaryTree(node1)) 
    print(Solution().widthOfBinaryTree2(node1)) 


if __name__ == "__main__":
    main()