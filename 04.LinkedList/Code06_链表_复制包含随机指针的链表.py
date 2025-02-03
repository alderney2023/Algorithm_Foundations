## 测试链接 : https://leetcode.com/problems/copy-list-with-random-pointer/

#方法一：借用字典
def copyRandomList1(head):
    dic = {}
    cur = head
    while cur:
        dic[cur] = Node(cur.value)
        cur = cur.next
    cur = head
    while cur:
        dic[cur].next = dic.get(cur.next)
        dic[cur].random_next = dic.get(cur.random_next)
        cur = cur.next
    return dic[head]


#方法二：原地
def copyRandomList2(head):
    #创建新结点，next
    cur = head
    while cur:
        next = cur.next
        cur.next = Node(cur.value)
        cur.next.next = next
        cur = next 
    #赋值random_next
    cur = head
    while cur:  
        new = cur.next
        if cur.random_next: 
            new.random_next = cur.random_next.next
        cur = new.next
    #分离
    cur = head
    new_head = head.next  #新头
    while cur:  
        new = cur.next
        cur.next = new.next
        if new.next:
            new.next = new.next.next
        cur = cur.next
    return new_head


#---------------------------------------------------------------------------------

class Node:
    def __init__(self, value, next=None, random_next=None):
        self.value = value
        self.next = next
        self.random_next = random_next

def printLinkedList(head):
    cur = head
    while cur!=None:
        print(cur.value, end=" ")
        cur = cur.next
    print("")
    print("---------")

def main():
    node1 = Node(1)
    node2 = Node(2)
    node3 = Node(3)
    node1.next = node2
    node2.next = node3
    node3.next = None 
    node1.random_next = node3  
    node2.random_next = node1  
    node3.random_next = None 

    printLinkedList(node1)
    copy_head = copyRandomList1(node1)
    printLinkedList(node1)
    printLinkedList(copy_head)


    printLinkedList(node1)
    copy_head = copyRandomList2(node1)
    printLinkedList(node1)
    printLinkedList(copy_head)

    print(copy_head.value, copy_head.next.value, copy_head.next.next.value)
    print(copy_head.value, copy_head.next.random_next.value, copy_head.random_next.value)


if __name__ == "__main__":
    main()