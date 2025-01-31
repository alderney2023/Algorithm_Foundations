###########################################################################
# 反转单向链表
# 反转双向链表
###########################################################################

import random

# 反转单向链表
def reverseLinkedList(head):
    pre = None
    while head:
        next = head.next
        head.next = pre
        pre = head
        head = next
    return pre

# 反转双向链表
def reverseDoubleLinkedList(head):
    pre = None
    while head:
        next = head.next
        head.next = pre
        head.last = next
        pre = head
        head = next
    return pre




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
# 双向链表

class DoubleNode:
    def __init__(self, value=0, next=None, last=None):
        self.value = value
        self.next = next
        self.last = last

def generateRandomDoubleLinkedList(size, maxvalue):
    if size == 0 :
        return
    x = int (random.random() * (maxvalue + 1))
    head = cur = DoubleNode(x)
    for i in range(1, size):
        x = int (random.random() * (maxvalue + 1))
        new_node = DoubleNode(x)
        cur.next = new_node
        new_node.last = cur
        cur=cur.next
    return head

def printDoubleLinkedList(head, direction):
    if direction == 'next':
        cur = head
        while cur is not None:
            print(cur.value, end=" ")
            cur = cur.next
        print("")
    elif direction == 'last':
        cur = head
        while cur.next is not None:
            cur = cur.next
        while cur is not None:
            print(cur.value, end=" ")
            cur = cur.last 
        print("")     
    print("---------")

#---------------------------------------------------------------------------------

def main():
    
    print("单向链表")
    size = 5
    maxvalue = 10
    head = generateRandomLinkedList(size, maxvalue)
    printLinkedList(head)
    new_head = reverseLinkedList(head)
    printLinkedList(new_head)

    print("双向链表")
    size = 5
    maxvalue = 10
    head = generateRandomDoubleLinkedList(size, maxvalue)
    printDoubleLinkedList(head,"next")
    printDoubleLinkedList(head,"last")

    new_head = reverseDoubleLinkedList(head)
    printDoubleLinkedList(new_head,"next")
    printDoubleLinkedList(new_head,"last")

if __name__ == "__main__":
    main()