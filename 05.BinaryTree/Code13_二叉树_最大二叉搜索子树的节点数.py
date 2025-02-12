###########################################################################
# 给定一棵二叉树的头节点head, 任
# 返回这棵二叉树中最大的二叉搜索子树的头节点
###########################################################################


class info:
    def __init__(self, isBST,maxV, minV, maxSize):
        self.isBST = isBST
        self.maxV = maxV
        self.minV = minV
        self.maxSize = maxSize

def maxSubBST(head): 
    if not head:
        return 0 
    return process(head).maxSize

def process(head):
    if not head:
        return None
    leftInfo = process(head.left)
    rightInfo = process(head.right)

    maxV = minV = head.value
    maxSize = 0
    if leftInfo:
        maxV = max(maxV, leftInfo.maxV)
        minV = min(minV, leftInfo.minV)
        maxSize = max(maxSize, leftInfo.maxSize)
    if rightInfo:
        maxV = max(maxV, rightInfo.maxV)
        minV = min(minV, rightInfo.minV)    
        maxSize = max(maxSize, rightInfo.maxSize)   

    isBST = False
    if (not leftInfo or (head.value > leftInfo.maxV and leftInfo.isBST)) and \
        (not rightInfo or (head.value < rightInfo.minV and rightInfo.isBST))  :
        isBST = True
        maxSize = (leftInfo.maxSize if leftInfo else 0) + \
               (rightInfo.maxSize if rightInfo else 0) + 1
    
    return info(isBST, maxV, minV, maxSize)




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
    print(maxSubBST(head)) #1

    l2 = [4,2,6,1,3,5,7,None,None,None,None,None,None,None,None]
    head2 = buildByLevelQueue(l2)
    print(maxSubBST(head2)) #7

if __name__ == "__main__":
    main()