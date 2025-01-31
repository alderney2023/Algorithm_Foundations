###########################################################################
#奇数长度返回中点，偶数长度返回上中点 
#奇数长度返回中点，偶数长度返回下中点 
#奇数长度返回中点前一个，偶数长度返回上中点前一个 
#奇数长度返回中点前一个，偶数长度返回下中点前一个 
###########################################################################


#奇数长度返回中点，偶数长度返回上中点 
def midOrUpMidNode(head):
    if head is None :
        return head        # return head
    slow = head
    fast = head
    while fast.next and fast.next.next:
        slow = slow.next
        fast = fast.next.next
    return slow


#奇数长度返回中点，偶数长度返回下中点 
def midOrDownMidNode(head):
    if head is None or head.next is None :
        return head         # return head
    slow = head.next
    fast = head.next
    while fast.next and fast.next.next:
        slow = slow.next
        fast = fast.next.next
    return slow


#奇数长度返回中点前一个，偶数长度返回上中点前一个 
def midOrUpMidPreNode(head):
    if head is None or head.next is None or head.next.next is None:
        return None         # return None
    slow = head
    fast = head.next.next
    while fast.next and fast.next.next:
        slow = slow.next
        fast = fast.next.next
    return slow


#奇数长度返回中点前一个，偶数长度返回下中点前一个 
def midOrDownMidPreNode(head):
    if head is None or head.next is None:
        return None       # return None
    slow = head
    fast = head.next
    while fast.next and fast.next.next:
        slow = slow.next
        fast = fast.next.next
    return slow

#---------------------------------------------------------------------------------

#奇数长度返回中点，偶数长度返回上中点 
def midOrUpMidNode_check(head):
    if head is None:
        return None
    lst = []
    cur = head
    while cur:
        lst.append(cur)
        cur = cur.next
    i = (len(lst) - 1) >> 1
    return lst[i]


#奇数长度返回中点，偶数长度返回下中点 
def midOrDownMidNode_check(head):
    if head is None:
        return None
    lst = []
    cur = head
    while cur:
        lst.append(cur)
        cur = cur.next
    i = (len(lst)) >> 1
    return lst[i]

#奇数长度返回中点前一个，偶数长度返回上中点前一个 
def midOrUpMidPreNode_check(head):
    if head is None or head.next is None or head.next.next is None:
        return None
    lst = []
    cur = head
    while cur:
        lst.append(cur)
        cur = cur.next
    i = (len(lst)-3) >> 1
    return lst[i]

#奇数长度返回中点前一个，偶数长度返回下中点前一个 
def midOrDownMidPreNode_check(head):
    if head is None or head.next is None:
        return None
    lst = []
    cur = head
    while cur:
        lst.append(cur)
        cur = cur.next
    i = (len(lst)-2) >> 1
    return lst[i]


#---------------------------------------------------------------------------------

class Node:
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next


def main():
    
    #创建包含size个节点的链表
    size = 4
    head = cur = Node(0)
    for i in range(1, size):
        new_node = Node(i)
        cur.next = new_node
        #print(cur.value)
        cur=cur.next

    #打印链表的值
    cur = head
    while cur!=None:
        print(cur.value, end=" ")
        cur = cur.next
    print("")
    print("---------")

    #奇数长度返回中点，偶数长度返回上中点 
    ans1 = midOrUpMidNode(head)
    ans2 = midOrUpMidNode_check(head)
    print(ans1.value if ans1 else None, ans2.value if ans2 else None )

    ans1 = midOrDownMidNode(head)
    ans2 = midOrDownMidNode_check(head)
    print(ans1.value if ans1 else None, ans2.value if ans2 else None )

    ans1 = midOrUpMidPreNode(head)
    ans2 = midOrUpMidPreNode_check(head)
    print(ans1.value if ans1 else None, ans2.value if ans2 else None )

    ans1 = midOrDownMidPreNode(head)
    ans2 = midOrDownMidPreNode_check(head)
    print(ans1.value if ans1 else None, ans2.value if ans2 else None )


if __name__ == "__main__":
    main()