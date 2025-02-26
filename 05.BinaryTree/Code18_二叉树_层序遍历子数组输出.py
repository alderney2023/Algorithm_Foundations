###########################################################################
#二叉树的层序遍历, 子数组形式按层输出
# 输入：root = [3,9,20,null,null,15,7]
# 输出：[[3],[9,20],[15,7]]
#
# 方法一： 借用一个字典，和几个变量
# 方法二： 只借用几个变量
# 方法三： 不借用任何变量
#
# https://leetcode.cn/problems/binary-tree-level-order-traversal
###########################################################################

# Definition for a binary tree node.

# 方法一： 借用一个字典，和几个变量
def levelOrder1(root):
    if not root: 
        return []
    dic_level = {}
    dic_level[root] = 1
    queue = [root]
    curLevel = 1
    res = []
    subres= []
    
    while queue:
        cur = queue.pop(0)
        nodeLevel = dic_level[cur]
        
        if cur.left:
            queue.append(cur.left)
            dic_level[cur.left] = nodeLevel + 1
        if cur.right:
            queue.append(cur.right)
            dic_level[cur.right] = nodeLevel + 1

        if nodeLevel == curLevel:
            subres.append(cur.val)
        else: 
            res.append(subres)
            subres = []
            subres.append(cur.val)
            curLevel += 1
    if subres:
        res.append(subres)
    return res



# 方法二： 只借用几个变量
def levelOrder2(root):
    if not root: 
        return []
    queue = [root]
    res = []
    subres= []
    curLevelEnd = root
    nextLevelEnd = None
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
            res.append(subres)
            subres = []
            if nextLevelEnd:
                curLevelEnd = nextLevelEnd
    return res


# 方法三： 不借用任何变量
def levelOrder3(root):
    if not root: 
        return []
    queue = [root]
    res = []
    while queue:
        subres = []
        for i in range(len(queue)):
            cur = queue.pop(0)
            subres.append(cur.val)
            if cur.left:
                queue.append(cur.left)
            if cur.right:
                queue.append(cur.right)
        res.append(subres)
    return res



#---------------------------------------------------------------------------------

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