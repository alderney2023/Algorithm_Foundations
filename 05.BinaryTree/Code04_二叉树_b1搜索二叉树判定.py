###########################################################################
# 二叉查找树（Binary Search Tree），（又：二叉搜索树，二叉排序树）
#   它或者是一棵空树，或者是具有下列性质的二叉树： 
#       若它的左子树不空，则左子树上所有结点的值均小于它的根结点的值； 
#       若它的右子树不空，则右子树上所有结点的值均大于它的根结点的值； 
#       它的左、右子树也分别为二叉搜索树
#
#   方法一： 递归法， 在每个节点上核查BST的三项是否符合
#   方法二： 递归中序遍历，存入栈，再比较
#   方法三： 递归中序遍历， 借用一个全局变量记录前一个值
#   方法四： 非递归中序遍历，和前一个值比较
###########################################################################


# 方法一： 递归法， 在每个节点上核查BST的三项是否符合
class info:
    def __init__(self, isBST, minV, maxV):
        self.isBST = isBST
        self.minV = minV
        self.maxV = maxV

def isBST(head):
    if not head:
        return True
    res = processBST(head)
    return res.isBST 
    
# def processBST(head):
#     if not head:
#         return None

#     l = processBST(head.left)
#     r = processBST(head.right)  

#     isBST = True
#     maxV = head.value
#     minV = head.value
#     if l:
#         minV = min(minV, l.minV)
#         maxV = max(maxV, l.maxV)
#         if (not l.isBST) or l.maxV >= head.value:
#             isBST = False
#     if r:
#         minV = min(r.minV, head.value)
#         maxV = max(r.maxV, head.value)
#         if (not r.isBST) or r.minV <= head.value:
#             isBST = False
#     return info(isBST, minV, maxV)

def processBST(root):
    if not root:
        return info(True, float("inf") , -float("inf"))
    leftInfo = processBST(root.left)
    rightInfo = processBST(root.right)
    maxV = max(leftInfo.maxV, rightInfo.maxV, root.value)
    minV = min(leftInfo.minV, rightInfo.minV, root.value)
    isBST = False
    if root.value > leftInfo.maxV and root.value < rightInfo.minV and leftInfo.isBST and rightInfo.isBST:
        isBST = True
    return info(isBST, minV, maxV)



# 方法二： 递归中序遍历，存入栈，再比较
def isBST2(head):
    if not head:
        return None
    stack = []
    inOrder(head,stack)
    for i in range(1, len(stack)):
        if stack[i].value <= stack[i-1].value:
            return False
    return True

def inOrder(head, stack):
    if not head:
        return
    inOrder(head.left, stack)
    stack.append(head)
    inOrder(head.right, stack)


# 方法三： 递归中序遍历， 借用一个全局变量记录前一个值

preV = -float('inf')

def isBST3(head):
    if not head:
        return True
    left = isBST3(head.left)
    global preV
    if not left:
        return False
    if head.value <= preV:
        return False
    else:
        preV = head.value
    return isBST3(head.right)


# 方法四：中序遍历，非递归法

def isBST4(head):
    if not head:
        return True
    preV = -float('inf')
    stack = []
    while head or stack:
        if head:
            stack.append(head)
            head = head.left
        else:
            head = stack.pop()
            if head.value <= preV:
                return False
            else:
                preV = head.value
            head = head.right

    return True



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
    head.right.left = Node(6)
    head.right.right = Node(7)

    print(isBST(head))
    print(isBST2(head))
    global preV 
    preV= -float('inf')
    print(isBST3(head))
    print(isBST4(head))

    head2 = Node(4)
    head2.left = Node(2)
    head2.right = Node(6)
    head2.left.left = Node(1)
    head2.left.right = Node(3)
    head2.right.left = Node(5)
    head2.right.right = Node(7)

    print(isBST(head2))
    print(isBST2(head2))
    #global preV 
    preV = -float('inf')
    print(isBST3(head2))
    print(isBST4(head2))


if __name__ == "__main__":
    main()