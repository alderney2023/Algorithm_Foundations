############################################################################
# 二叉树中的链表
# 给你一棵以root为根的二叉树、一个以head为头的链表
# 在二叉树中，有很多一直向下的路径
# 如果某个路径上的数值等于以head为头的整个链表
# 返回True，否则返回False
#
# 测试链接 : https://leetcode.cn/problems/linked-list-in-binary-tree/
############################################################################

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSubPath(self, head, root):
        m = 0 
        s2 = []
        cur = head
        while cur:
            m += 1
            s2.append(cur.val)
            cur = cur.next
        next = self.nextArr(s2)
        return self.find(s2, next, root, 0)
    
    def find(self, s2, next, cur, i):
        if i == len(s2):
            return True
        if not cur:
            return False
        while i >= 0 and cur.val != s2[i]:
            i = next [i]
        return self.find(s2, next, cur.left, i+1) or self.find(s2, next, cur.right, i+1)

    def nextArr(self, s):
        m = len(s)
        if m == 1:
            return [-1]
        next = [0] * m
        next[0] = -1
        next[1] = 0
        i = 2 
        cn = 0
        while i < m: 
            if s[i-1] == s[cn]:
                next[i] = cn+1
                i += 1
                cn += 1
            elif cn == 0:
                next[i] = 0
                i += 1
            else:
                cn = next[cn]
        return next