###########################################################################
# 删除链表中所有值为给定值n的结点
#   方法一： 删除开头的所有n, 再删除之后出现的n
#   方法二： 增加dummy结点， 删除所有出现的n
###########################################################################

# 方法一： 删除开头的所有n, 再删除中间的n
def deleteNode(head, value):
    if head is None:  #处理空链表
        return
    while head.value == value: # 处理只包含特定值的链表， 返回空链表
        head = head.next
        if head is None:
            return head

    #第一个值一定不是特定值，开始正常处理
    cur = head
    while cur and cur.next:
        if cur.next.value == value:
            cur.next = cur.next.next
        cur = cur.next
    return head


# 方法二： 增加dummy结点， 删除所有中间的n
def deleteNode2(head, value):
    dummy = Node(0)
    dummy.next = head
    
    prev, cur = dummy, head
    while cur:
        if cur.value == value:
            prev.next = cur.next
        else:
            prev = cur
        cur = cur.next
    return dummy.next


#---------------------------------------------------------------------------------

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

def listToLinkedList(lst):
    if not lst:
        return 
    head = cur = Node(lst[0])
    for i in range(1, len(lst)):
        new_node = Node(lst[i])
        cur.next = new_node
        #print(cur.value)
        cur=cur.next
    return head

def main():
    
    #创建包含size个节点的链表
    lst = [4,1,4,3,4,4,4,4]
    head = listToLinkedList(lst)


    printLinkedList(head)
    #head = deleteNode(head, 4)
    head = deleteNode2(head, 4)
    printLinkedList(head)

if __name__ == "__main__":
    main()