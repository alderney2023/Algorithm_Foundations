###########################################################################
# 中序遍历，查找某节点的后序节点
#    1.如果此节点有右节点，则后序节点为： 此节点右节点的最左节点
#    2 如果此节点没有右节点，则后序节点为： 此节点在某个父节点（后序节点）的左子树上
###########################################################################


def InOrderSuccessorNode(head, node):
    if node.right:
        cur = node.right
        while cur.left:
            cur = cur.left
        return cur
    else:
        cur = node
        parent = cur.parent
        while parent and parent.left != cur:
            cur = parent
            parent = parent.parent
        return parent


#---------------------------------------------------------------------------------   

class Node:
    def __init__(self, value=0, left=None, right=None, parent=None):
        self.value = value
        self.left = left
        self.right = right
        self.parent = parent

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

def main():

    head = Node(6)
    head.parent = None
    head.left = Node(3)
    head.left.parent = head
    head.left.left = Node(1)
    head.left.left.parent = head.left
    head.left.left.right = Node(2)
    head.left.left.right.parent = head.left.left
    head.left.right = Node(4)
    head.left.right.parent = head.left
    head.left.right.right = Node(5)
    head.left.right.right.parent = head.left.right
    head.right = Node(9)
    head.right.parent = head;
    head.right.left = Node(8)
    head.right.left.parent = head.right
    head.right.left.left = Node(7)
    head.right.left.left.parent = head.right.left
    head.right.right = Node(10)
    head.right.right.parent = head.right

    printTree(head)

    print(InOrderSuccessorNode(head, head.right).value)  #9,10
    print(InOrderSuccessorNode(head, head.left.right.right).value) #5,6
    print(InOrderSuccessorNode(head, head.right.right)) #10, None


if __name__ == "__main__":
    main()