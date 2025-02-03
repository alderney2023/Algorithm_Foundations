
###########################################################################
# 将链表按小于n,等于n,大于n排序
# 方法一： 拆成三个链表，再连接
# 方法二： 转成列表，做partition，再转成链表
###########################################################################

import random

def listPartition1(head, n):
    if not head or not head.next:
        return head
    sh,st,eh,et,bh,bt = None, None, None, None, None, None
    while head:
        next = head.next
        head.next = None
        if head.value < n:
            if not sh:
                sh = head
                st = head
            else:
                st.next = head
                st = head
        elif head.value == n:
            if not eh:
                eh = head
                et = head
            else:
                et.next = head
                et = head
        else:
            if not bh:
                bh = head
                bt = head
            else:
                bt.next = head
                bt = head
        head = next

    if st:
        st.next = eh
        if not et:
            et = st
    if et:
        et.next = bh     
    if sh:
        return sh
    elif eh:
        return eh
    else:
        return bh
        


#方法二： 转成列表，荷兰国旗问题
def listPartition2(head, n):  
    if not head or not head.next:
        return head
    #转成列表，调用partition  
    lst = []
    cur = head
    while cur:
        lst.append(cur)
        cur = cur.next
    partition(lst, n)
    #将列表按顺序串成链表
    for i in range(len(lst)-1):
        lst[i].next = lst[i+1]
    lst[-1].next = None
    return lst[0]


def partition(lst, n):
    less = -1
    more = len(lst)
    i = 0
    while i < more:
        if lst[i].value < n:
            lst[i], lst[less+1] = lst[less+1], lst[i]
            less+=1
            i+=1
        elif lst[i].value > n:
            lst[i], lst[more-1] = lst[more-1], lst[i]
            more-=1
        else:
            i+=1



#---------------------------------------------------------------------------------
#单向链表

class Node:
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next

def printLinkedList(head):
    cur = head
    while cur!=None:
        print(cur.value, end=" ")
        cur = cur.next
    print("")
    print("---------")

def generateRandomLinkedList(size, maxvalue):
    if size == 0 :
        return
    x = int (random.random() * (maxvalue + 1))
    head = cur = Node(x)
    for i in range(1, size):
        x = int (random.random() * (maxvalue + 1))
        new_node = Node(x)
        cur.next = new_node
        cur=cur.next
    return head

#---------------------------------------------------------------------------------

def main():

    size = 10
    maxvalue = 10
    head = generateRandomLinkedList(size, maxvalue)
    printLinkedList(head)
    head = listPartition1(head, 9)
    printLinkedList(head)

    # head = generateRandomLinkedList(size, maxvalue)
    # printLinkedList(head)
    # head = listPartition2(head, 5)
    # printLinkedList(head)


if __name__ == "__main__":
    main()