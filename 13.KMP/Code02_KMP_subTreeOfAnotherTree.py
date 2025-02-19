############################################################################
# 另一棵树的子树
# 给你两棵二叉树root和subRoot
# 检验root中是否包含和subRoot具有相同结构和节点值的子树
# 如果存在，返回true
# 否则，返回false
# 
# 测试链接 : https://leetcode.cn/problems/subtree-of-another-tree/
############################################################################

class TreeNode:
    def __init__(self, val, left=None, right= None):
        self.val = val
        self.left = left
        self.right = right


#--------------------------------------------------------------------------
#  递归

def isSubTree1(t1, t2):
    if not t2:  # An empty tree is always a subtree
        return True
    if not t1:  # t1 is empty but t2 is not, so return False
        return False
    if isSameTree(t1, t2):
        return True
    return isSubTree(t1.left, t2) or isSubTree(t1.right, t2)

def isSameTree(t1, t2):
    if not t1 and not t2:
        return True
    if not t1 or not t2:
        return False
    return t1.val == t2.val and isSameTree(t1.left, t2.left) and isSameTree(t1.right, t2.right)


#--------------------------------------------------------------------------
# KMP

def isSubTree(t1, t2):
    if not t2:
        return True
    elif not t1:
        return False
    else:    #t1 and t2
        s1 = []
        serialPre(t1, s1)
        s2 = []
        serialPre(t2, s2)
        return kmp(s1,s2) != -1

def serialPre(t, s):
    if not t:
        s.append(None)
    else:
        s.append(t.val)
        serialPre(t.left, s)
        serialPre(t.right, s)


def kmp(s1, s2):
    n = len(s1)
    m = len(s2)
    next = nextArr(s2)
    x,y = 0, 0
    while x<n and y<m:
        if isEqual(s1[x],s2[y]):
            x+=1
            y+=1
        elif y==0:
            x+=1
        else:
            y = next[y]
    
    if y==m:
        return x-y
    else:
        return -1

def nextArr(s):
    m = len(s)
    if m == 1:
        return [-1]
    next = [0] * m
    next[0] = -1
    next[1] = 0 
    i = 2
    cn = 0 
    while i < m:
        if isEqual(s[i-1],s[cn]):
            next[i] = cn+1
            i+=1
            cn+=1
        elif cn == 0:
            next[i] = 0
            i+=1
        else:
            cn = next[cn]
    return next


# def isEqual(a,b):
#     if not a and not b:
#         return True
#     elif a != None and b != None:
#         return a == b
#     else:
#         return False

def isEqual(s1, s2):  # 判断None比较
    if s1 == None and s2 == None:
        return True
    elif s1 ==None or s2 == None:
        return False
    else:
        return s1 == s2

def main():

    # Node1 = TreeNode(1)
    # Node2 = TreeNode(2)
    # Node3 = TreeNode(3)
    # Node4 = TreeNode(4)
    # Node5 = TreeNode(5)
    # Node4.left = Node1
    # Node4.right = Node2
    # Node3.left = Node4
    # Node3.right = Node5
    # root = Node3
    # SubRoot = Node4
    # print(isSubTree(root, SubRoot))

    Node00 = TreeNode(0)
    Node01 = TreeNode(1)
    Node02 = TreeNode(2)
    Node03 = TreeNode(3)
    Node04 = TreeNode(4)
    Node05 = TreeNode(5)
    Node02.left = Node00
    Node04.left = Node01
    Node04.right = Node02
    Node03.left = Node04
    Node03.right = Node05
    root = Node03
    Node1 = TreeNode(1)
    Node2 = TreeNode(2)
    Node4 = TreeNode(4)
    Node4.left = Node1
    Node4.right = Node2
    SubRoot = Node4

    # s1,s2 = [], []
    # serialPre(root, s1)
    # serialPre(SubRoot, s2)
    # print(s1)
    # print(s2)

    print(isSubTree(root, SubRoot))






if __name__ == "__main__":
    main()