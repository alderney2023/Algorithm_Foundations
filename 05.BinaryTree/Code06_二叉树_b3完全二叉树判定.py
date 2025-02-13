###########################################################################
# 完全二叉树的定义如下：
# 在完全二叉树中，除了最底层节点可能没填满外，其余每层节点数都达到最大值，
# 并且最下面一层的节点都集中在该层最左边的若干位置

#https://leetcode.com/problems/check-completeness-of-a-binary-tree/

###########################################################################

# 方法一：按层遍历过程中判断

def isCBT(head):
    if not head:
        return True
    stack = []
    stack.append(head)
    leaf = False
    while stack:
        head = stack.pop()
        if (not head.left and head.right) or (leaf and (head.left or head.right)):
            return False
        if head.left:
            stack.append(head.left)
        if head.right:
            stack.append(head.right)
        if not head.left or not head.right:   # ***
            left = True
    return True


#---------------------------------------------------------------------------------

# 方法二：二叉树递归套路

class info:
    def __init__(self,isFull, isCBT, height):
        self.isFull = isFull
        self.isCBT = isCBT
        self.height = height

def isCBT2(head):
    if not head:
        return None
    return process(head).isCBT

def process(head):
    if not head:
        return info(True, True, 0)
    
    leftInfo = process(head.left)
    rightInfo = process(head.right)

    height = max(leftInfo.height, rightInfo.height) + 1
    isFull = False
    if leftInfo.isFull and rightInfo.isFull and leftInfo.height == rightInfo.height:
        isFull = True
    isCBT = False

    #满二叉树（无缺口，左满，右满，左右在同层）
    #缺口在左，左不满，右满，左比右高一层
    #缺口在左，左满，右满，左比右高一层
    #缺口在右，左满，右不满，左右在同层
    if isFull or\
       (leftInfo.isCBT and rightInfo.isFull and leftInfo.height == rightInfo.height + 1) or\
       (leftInfo.isFull and rightInfo.isFull and leftInfo.height == rightInfo.height + 1) or\
       (leftInfo.isFull and rightInfo.isCBT and leftInfo.height == rightInfo.height):
        isCBT = True
    return info(isFull, isCBT, height)

   


#---------------------------------------------------------------------------------

class Node:
    def __init__(self, value=0, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

def main():
    head = Node(1)
    head.left = Node(2)
    head.right = Node(3)
    head.left.left = Node(4)
    head.left.right = Node(5)
    #head.right.left = Node(6)
    head.right.right = Node(7)

    print(isCBT(head))
    print(isCBT2(head))
    


if __name__ == "__main__":
    main()