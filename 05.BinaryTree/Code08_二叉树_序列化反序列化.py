
#-----------------------------------
#            序列化 
#-----------------------------------


# 先序序列化 
def preSerial(head):
    lst = []
    preSerialProcess(head, lst)
    return lst

def preSerialProcess(head, lst):
    if not head:
        lst.append(None)
        return
    lst.append(head.value)
    preSerialProcess(head.left, lst)
    preSerialProcess(head.right, lst)
    

# 后序序列化 
def posSerial(head):
    lst =[]
    posSerialProcess(head, lst)
    return lst

def posSerialProcess(head, lst):
    if not head:
        lst.append(None)
        return
    posSerialProcess(head.left, lst)
    posSerialProcess(head.right, lst)
    lst.append(head.value)


#宽度序列化
# 方法一： None入队列
def levelSerial1(head):
    if not head:
        return None
    queue = [head]
    res = []
    while queue :  
        head = queue.pop(0)
        if head:
            res.append(head.value)
            queue.append(head.left)
            queue.append(head.right)
        else: 
            res.append(None)
    return res


# 方法一： None不入队列
def levelSerial2(head):
    if not head:
        return None
    queue = [head]
    res = [head.value]
    while queue :  
        head = queue.pop(0)
        if head.left:
            queue.append(head.left)
            res.append(head.left.value)
        else:
            res.append(None)
        if head.right:
            queue.append(head.right)
            res.append(head.right.value)
        else: 
            res.append(None)
    return res



#-----------------------------------
#              反序列化
#-----------------------------------


# 先序反序列化
def preBuild(lst):
    if not lst or len(lst) == 0:
        return None
    return preBuildProcess(lst)

def preBuildProcess(lst):
    v = lst.pop(0)
    if not v:
        return None
    head = Node(v)
    head.left = preBuildProcess(lst)
    head.right = preBuildProcess(lst)
    return head


# 后序反序列化   lst(左右中) 反转即为 （中右左）
def posBuild(lst):
    if not lst or len(lst) == 0:
        return None
    return posBuildProcess(lst)

def posBuildProcess(lst):
    v = lst.pop()
    if not v:
        return None
    head = Node(v)
    head.right = posBuildProcess(lst)
    head.left = posBuildProcess(lst)
    return head


#宽度反序列化
def levelBuild(lst):
    if not lst or len(lst)==0:
        return None
    queue = []
    head = generateNode(lst.pop(0))
    if head:
        queue.append(head)
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

class Node:
    def __init__(self, value=0, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

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
    pre_lst = [1, 2, None, None, 3, None, None]
    head = preBuild(pre_lst)
    printTree(head)
    res = preSerial(head)
    print(res)

    pos_lst = [None, None, 2, None, None, 3, 1]
    head = posBuild(pos_lst)
    printTree(head)
    res = posSerial(head)
    print(res)

    level_lst = [1, 2, 3, 4, None, 6, 7, None, None, None, None, 8 , 9, None, None, None, None]
    head = levelBuild(level_lst)
    printTree(head)
    res = levelSerial1(head)
    print(res)
    res = levelSerial2(head)
    print(res)

if __name__ == "__main__":
    main()