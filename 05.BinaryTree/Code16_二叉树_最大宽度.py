###########################################################################
# 最大宽度
# 方法一： 借用一个字典和几个变量
# 方法二： 只借用几个变量
###########################################################################

import random

# 方法一： 借用一个字典和几个变量
def maxWidthUseDic(head):
    if not head:
        return
        
    dic_level = {}
    dic_level[head] = 1
    curLevel = 1
    curNodes = 0
    maxNodes = 0 
    queue = []
    queue.append(head)
    while queue:
        head = queue.pop(0)
        nodeLevel = dic_level.get(head)

        if head.left:
            dic_level[head.left] = nodeLevel + 1
            queue.append(head.left)
        if head.right:
            dic_level[head.right] = nodeLevel + 1
            queue.append(head.right)

        if nodeLevel == curLevel:
            curNodes += 1
        else:
            maxNodes = max(maxNodes,curNodes)
            curNodes = 1
            curLevel +=1
    maxNodes = max(maxNodes,curNodes)
    return maxNodes    
      

# 方法二： 只借用几个变量
def maxWidthNoDic(head):
    if not head:
        return

    curEnd = head
    nextEnd = None
    curNodes = 0
    maxNodes = 0 
    queue = []
    queue.append(head)
    while queue:
        head = queue.pop(0)

        if head.left:
            nextEnd = head.left
            queue.append(head.left)
        if head.right:
            nextEnd = head.right
            queue.append(head.right)
     
        curNodes += 1
        if head == curEnd:   # ***
            maxNodes = max(maxNodes,curNodes)
            curNodes = 0
            curEnd = nextEnd
    return maxNodes   


#---------------------------------------------------------------------------------

class Node:
    def __init__(self, value=0, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

# 创建二叉树
def generateRandomBT(maxLevel, maxValue):
	return generate(1, maxLevel, maxValue)

def generate(level, maxLevel, maxValue):
	if (level > maxLevel or random.random() < 0.5):
		return None
	head = Node((int)(random.random() * maxValue))
	head.left = generate(level + 1, maxLevel, maxValue)
	head.right = generate(level + 1, maxLevel, maxValue)
	return head


#打印二叉树
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

def main():
    # head = Node(1)
    # head.left = Node(2)
    # head.right = Node(3)
    # head.left.left = Node(4)
    # head.left.right = Node(5)
    # head.right.left = Node(6)
    # head.right.right = Node(7)

    # level(head)
    # print(maxWidthUseDic(head))
    # print(maxWidthNoDic(head))


    head2 = generateRandomBT(10, 100)
    print(maxWidthUseDic(head2))
    print(maxWidthNoDic(head2))
    #printTree(head2)

if __name__ == "__main__":
    main()