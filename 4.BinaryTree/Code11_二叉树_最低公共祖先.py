###########################################################################
# 查找树中两节点的最低公共节点
#    方法一： 直接递归查找，不易理解
#    方法二： 借用一个字典，存储每个节点的父节点
###########################################################################


#方法一： 直接递归查找，不易理解
def LowestCommonAncestor(head, o1, o2):
    if not head or head==o1 or head==o2:
        return head
    left = LowestCommonAncestor(head.left, o1, o2)
    right = LowestCommonAncestor(head.right, o1, o2)
    if left and right:
        return head
    if left:
        return left
    else:
        return right


# 方法二： 借用一个字典，存储每个节点的父节点
def LowestCommonAncestor2(head, o1, o2):
    if not head:
        return None
    #存储每个点的父节点， 头节点的父设为None
    dic = {}  
    dic[head] = None  
    processPre(head, dic)
    # 存储o1的所有父节点
    s = set()  
    cur = o1
    s.add(cur)
    while dic.get(cur):
        cur = dic[cur]
        s.add(cur)
    #网上遍历o2的父节点，第一个在s中出现的即为答案，如果一直走的head的父，就说明没有，返回None
    cur = o2
    while cur not in s:
        cur = dic.get(cur)
    return cur

def processPre(head, dic):
    if not head:
        return 
    if head.left:
        dic[head.left] = head
        processPre(head.left, dic)
    if head.right:
        dic[head.right] = head
        processPre(head.right, dic)


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

    print(LowestCommonAncestor(head, head.left , head.left.right).value)
    print(LowestCommonAncestor(head, head.left.left , head.right.right).value)
   
    print(LowestCommonAncestor2(head, head.left , head.left.right).value)
    print(LowestCommonAncestor2(head, head.left.left , head.right.right).value)


if __name__ == "__main__":
    main()