###########################################################################
# 给定一棵二叉树的头节点head, 任何两个节点之间都存在距离，
# 返回整棵二叉树的最大距离
#
# https://leetcode.cn/problems/diameter-of-binary-tree
###########################################################################

class info:
    def __init__(self, height, maxdistance):
        self.height = height
        self.maxdistance = maxdistance

def maxDistance(head):
    if not head:
        return 0
    return process(head).maxdistance

def process(head):
    if not head:
        return info(0,0)
    left = process(head.left)
    right = process(head.right)
    height = max(left.height, right.height) + 1
    maxdistance = max(left.maxdistance,right.maxdistance, left.maxdistance + right.maxdistance + 1)
    return info(height, maxdistance)
    

#---------------------------------------------------------------------------------   

class Node:
    def __init__(self, value=0, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

def buildByLevelQueue(lst):
    if not lst:
        return
    
    head = generateNode(lst.pop(0))
    if head:
        queue = [head]
    while queue:
        cur = queue.pop(0)
        cur.left = generateNode(lst.pop(0))
        cur.right = generateNode(lst.pop(0))
        if cur.left:
            queue.append(cur.left)
        if cur.right:
            queue.append(cur.right)
    return head

def generateNode(val):
    if val == None:
        return None
    return Node(val)


#--------------------------------------------------------------------------------- 

def main():
    l= [1,2,3,4,5,6,7,None,None,None,None,None,None,None,None]
    head = buildByLevelQueue(l)
    print(maxDistance(head)) #7

    l2 = [1,2,3, None, 4, 5, None, None, None, None, 6, None, None]
    head2 = buildByLevelQueue(l2)
    print(maxDistance(head2)) #6

if __name__ == "__main__":
    main()