###########################################################################
# 完全二叉树的定义如下：
# 在完全二叉树中，除了最底层节点可能没填满外，其余每层节点数都达到最大值，
# 并且最下面一层的节点都集中在该层最左边的若干位置

#https://leetcode.com/problems/check-completeness-of-a-binary-tree/

###########################################################################


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
    


if __name__ == "__main__":
    main()