###########################################################################
# 深度优先遍历
#   非递归遍历：先序，中序，后序
#   递归遍历：先序，中序，后序
###########################################################################

#非递归遍历：先序
def nonRecursivePre(head):
    if not head:
        return
    stack = []
    stack.append(head)
    while stack:
        head = stack.pop()
        print(head.value, end=" ")
        if head.right:
            stack.append(head.right)
        if head.left:
            stack.append(head.left)
    print()


#非递归遍历：中序 ***
def nonRecursiveIn(head):
    if not head:
        return
    stack = []
    while head or stack:
        if head:
            stack.append(head)
            head = head.left
        else:
            head = stack.pop()
            print(head.value, end=" ")    
            head = head.right 
    print()
            

#非递归遍历：后序
def nonRecursivePos(head):
    if not head:
        return
    stack = []
    stack.append(head)
    stack_res = []
    while stack:
        head = stack.pop()
        stack_res.append(head)
        if head.left:
            stack.append(head.left)
        if head.right:
            stack.append(head.right)
    while stack_res:
        cur = stack_res.pop()
        print(cur.value, end=" ")
    print()
        

#非递归遍历：后序  ***
def nonRecursivePos2(head):
    if not head:
        return
    stack = []
    stack.append(head)
    while stack:
        peek = stack[-1]
        if peek.left and peek.left!=head and peek.right!=head:
            stack.append(peek.left)
        elif peek.right and peek.right!=head:
            stack.append(peek.right)
        else:
            print(stack.pop().value, end=" ")
            head = peek
    print()
        


#---------------------------------------------------------------------------------

#递归遍历： 先序
def recursivePre(head):
    if not head:
        return None
    print(head.value, end=" ")
    recursivePre(head.left)
    recursivePre(head.right)


#递归遍历： 中序
def recursiveIn(head):
    if not head:
        return None
    recursiveIn(head.left)
    print(head.value, end=" ")
    recursiveIn(head.right)


#递归遍历： 后序
def recursivePos(head):
    if not head:
        return None
    recursivePos(head.left)
    recursivePos(head.right)
    print(head.value, end=" ")


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

    nonRecursivePre(head)
    recursivePre(head)
    print()
    nonRecursiveIn(head)
    recursiveIn(head)
    print()
    nonRecursivePos(head)
    nonRecursivePos2(head)
    recursivePos(head)
    print()


if __name__ == "__main__":
    main()
