
# 判断链表是否为回文
# 方法一： need n extra space
# 方法二： need n/2 extra space
# 方法三： need O(1) extra space



# 方法一： need n extra space
def isPalindrome1(head):
    stack = []
    cur = head
    while cur:
        stack.append(cur)
        cur = cur.next
    while stack:
        if stack.pop().value != head.value:
            return False
        head = head.next
    return True



# 方法二： need n/2 extra space
def isPalindrome2(head):
    if not head:
        return True
    #中点or上中点
    slow = head
    fast = head
    while fast.next and fast.next.next:
        slow = slow.next
        fast = fast.next.next
    #从中点or上中点下一个入栈
    stack = []
    cur = slow.next
    while cur:
        stack.append(cur)
        cur = cur.next
    #栈中数据与链表开头开始比较
    while stack:
        if stack.pop().value != head.value:
            return False
        head = head.next
    return True


# 方法三： need O(1) extra space

def isPalindrome3(head):
    if not head:
        return True
    #中点or上中点
    slow = head
    fast = head
    while fast.next and fast.next.next:
        slow = slow.next
        fast = fast.next.next
    
    #反转后半部分
    cur = slow.next  #右半部分第一个node
    slow.next = None   #中点or上中点.next -> None
    prev = slow      #中点or上中点
    while cur:
        next = cur.next
        cur.next = prev
        prev = cur
        cur = next
    #从两头向中间遍历进行比较
    res = True
    tail = prev   # tail为保存指向最后一个结点的指针
    cur = head
    while prev:
        if cur.value != prev.value:
            res = False
            break
        cur = cur.next
        prev = prev.next

    prev = None
    cur = tail 
    while cur:
        next = cur.next
        cur.next = prev
        prev = cur
        cur = next

    return res
       

#---------------------------------------------------------------------------------


class Node:
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next

def printLinkedList(head):
    cur = head
    while cur!=None:
       # print(cur.value, end=" ")
        cur = cur.next
    #print("")
    #print("---------")

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
    
    lsts = ['abcdcba', '','a', 'abcd']
    for s in lsts:
        head = listToLinkedList(s)
        #printLinkedList(head)
        #print(isPalindrome2(head))

        printLinkedList(head)
        print(isPalindrome3(head))
        printLinkedList(head)


if __name__ == "__main__":
    main()