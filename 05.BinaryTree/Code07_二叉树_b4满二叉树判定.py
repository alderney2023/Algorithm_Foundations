###########################################################################
# 满二叉树：
#     如果一棵二叉树只有度为0的结点和度为2的结点
#     并且度为0的结点在同一层上
###########################################################################


# 第一种方法
# 收集整棵树的高度h，和节点数n
# 只有满二叉树满足 : 2 ^ h - 1 == n
class info:
    def __init__(self, height, n):
        self.height = height    #树的高度
        self.n = n              #节点数

def isFull(head):
    if not head:
        return True
    x = process(head)
    return  (1 << x.height) - 1 == x.n

def process(head):
    if not head:
        return info(0,0)
    l = process(head.left)
    r = process(head.right)
    height = max(l.height, r.height)+1
    n = l.n + r.n + 1
    return info(height, n)


# 第二种方法
# 收集子树是否是满二叉树
# 收集子树的高度
# 左树满 && 右树满 && 左右树高度一样 -> 整棵树是满的
class info2:
    def __init__(self, height, isFull):
        self.height = height    #树的高度
        self.isFull = isFull       

def isFull2(head):
    if not head:
        return True
    x = process2(head)
    return x.isFull
    
def process2(head):
    if not head:
        return info2(0,True)
    l = process2(head.left)
    r = process2(head.right)
    height = max(l.height, r.height) + 1
    isFull = True
    if (not l.isFull) or (not r.isFull) or l.height != r.height:
        isFull = False 
    return info2(height, isFull)



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
    #head.right.right = Node(7)

    print(isFull(head))
    print(isFull2(head))


if __name__ == "__main__":
    main()