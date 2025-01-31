###########################################################################
#   平衡二叉树（Balanced Binary Tree）又被称为AVL树
#       它是一棵空树 或者是具有下列性质的二叉树：
#           它的左右两个子树的高度差的绝对值不超过1，
#           并且左右两个子树都是一棵平衡二叉树
###########################################################################

class info:
    def __init__(self, isBalance, height):
        self.isBalance = isBalance
        self.height = height

def isBalanced(head):
    # if not head:
    #     return True
    res = process(head)
    return res.isBalance

def process(head):
    if not head:
        return info(True,0)
    l = process(head.left)
    r = process(head.right)
    height = max(l.height, r.height) + 1 
    # if l.isBalance == False or r.isBalance == False or abs(l.height - r.height) > 1:
    #     isBalance = False
    isBalance = (l.isBalance and r.isBalance and abs(l.height - r.height) <= 1)
    return info(isBalance, height)



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

    print(isBalanced(head))


if __name__ == "__main__":
    main()