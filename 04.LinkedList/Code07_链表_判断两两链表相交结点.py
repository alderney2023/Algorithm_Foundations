###########################################################################
# 两个链表的首个相交交点
#     无环链表 和 无环链表 相交
#     无环链表 和 有环链表 相交  不存在
#     有环链表 和 有环链表 相交  在环外 在环内
###########################################################################


# 主调用函数
def getIntersectNode(head1, head2):
    if not head1 or not head2:
        return None
    loop1 = getLoopNode(head1)
    loop2 = getLoopNode(head2)
    if not loop1 and not loop2:
        return noLoop(head1, head2)
    elif loop1 and loop2:
        return bothLoop(head1, loop1, head2, loop2)
    return None

#找到单个链表的入环结点，如果无环返回None
def getLoopNode(head):
    if not head or not head.next or not head.next.next:
        return None
    slow = head.next
    fast = head.next.next
    while slow != fast:
        if not fast.next or not fast.next.next:   #
            return None
        slow = slow.next
        fast = fast.next.next
    fast = head
    while slow != fast:
        slow = slow.next
        fast = fast.next
    return slow

#如果两个链表都无环，返回第一个相交节点，如果不想交，返回None
def noLoop(head1, head2):
    m = 1
    cur1 = head1
    while cur1.next:
        m += 1
        cur1 = cur1.next
    n = 1
    cur2 = head2
    while cur2.next:
        n += 1 
        cur2 = cur2.next 
    if cur1 != cur2:
        return None

    if m >= n:
        long, short = head1, head2
    else:
        long, short = head2, head1
    dif = abs(m-n)
    for i in range(dif):
        long = long.next
    while long != short:
        long = long.next
        short = short.next
    return long

#两个有环链表，返回第一个相交节点，如果不想交返回None
def bothLoop(head1, loop1, head2, loop2):
    if loop1 != loop2:  #若相交，可能两个入环点
        cur1 = loop1.next
        while cur1 != loop1:
            if cur1 == loop2:
                return cur1
            cur1 = cur1.next
    else:  #若相交， 可能环外相交或同一个入环点
        cur, m = head1, 0
        while cur!= loop1.next:
            m += 1
            cur = cur.next
        cur, n = head2, 0
        while cur!= loop2.next:
            n += 1
            cur = cur.next
        if m >= n:
            long, short = head1, head2
        else:
            long, short = head2, head1
        dif = abs(m-n)
        for i in range(dif):
            long = long.next
        while long != loop1.next:
            if long == short:
                return long
            long = long.next
            short = short.next
    return None


#---------------------------------------------------------------------------------

class Node:
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next


def main():
        head1 = Node(1)
        head1.next = Node(2)
        head1.next.next = Node(3)
        head1.next.next.next = Node(4)
        head1.next.next.next.next = Node(5)
        head1.next.next.next.next.next = Node(6)
        head1.next.next.next.next.next.next = Node(7)


		# 0->9->8->6->7->null
        head2 = Node(0)
        head2.next = Node(9)
        head2.next.next = Node(8)
        head2.next.next.next = head1.next.next.next.next.next # 8->6
        print(getIntersectNode(head1, head2).value)


		# 1->2->3->4->5->6->7->4...
        head1 = Node(1)
        head1.next = Node(2)
        head1.next.next = Node(3)
        head1.next.next.next = Node(4)
        head1.next.next.next.next = Node(5)
        head1.next.next.next.next.next = Node(6)
        head1.next.next.next.next.next.next = Node(7)
        head1.next.next.next.next.next.next = head1.next.next.next # 7->4


		# 0->9->8->2...
        head2 = Node(0)
        head2.next = Node(9)
        head2.next.next = Node(8)
        head2.next.next.next = head1.next # 8->2
        print(getIntersectNode(head1, head2).value)

		# 0->9->8->6->4->5->6..
        head2 = Node(0)
        head2.next = Node(9)
        head2.next.next = Node(8)
        head2.next.next.next = head1.next.next.next.next.next # 8->6
        print(getIntersectNode(head1, head2).value)


if __name__ == "__main__":
    main()