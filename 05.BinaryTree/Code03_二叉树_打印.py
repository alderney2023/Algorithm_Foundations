###########################################################################
# 中序深度优先遍历打印二叉树
###########################################################################


def printTree(head):
    print("Binary Tree:")
    printInOrder(head, 0, 'H', 17)
    print()

def printInOrder(head, height, to, length):
    if not head:
        return
    printInOrder(head.right, height+1, "v", length)
    val = to + str(head.value) + to
    lenM = len(val)
    lenL = int ((length - lenM) / 2)
    lenR = length - lenM - lenL
    val = getSpace(lenL) + val + getSpace(lenR)
    print(getSpace(height * length) + val)
    printInOrder(head.left, height+1, "^", length)

def getSpace(n):
    return " " * n


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

    printTree(head)


if __name__ == "__main__":
    main()