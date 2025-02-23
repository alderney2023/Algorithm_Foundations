###########################################################################
# 排序链表
# 要求时间复杂度O(n*logn)，额外空间复杂度O(1)，还要求稳定性
# 数组排序做不到，链表排序可以
#
# 测试链接: https://leetcode.cn/problems/sort-list/
###########################################################################


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def sortList(head):
    if not head or not head.next:
        return head

    cur = head
    n = 0
    while cur:
        n += 1
        cur = cur.next

    step = 1
    while step < n:
        l1 = head 
        r1 = findEnd(l1, step)
        print(l1.val,r1.val)
        l2 = r1.next
        r2 = findEnd(l2,step)
        next_segment = r2.next

        r1.next = None
        r2.next = None
        start, end = merge(l1, r1, l2, r2)
        head = start
        lastTeamEnd = end

        while next_segment != None:
            l1 = next_segment
            r1 = findEnd(l1, step)
            l2 = r1.next
            if not l2:
                lastTeamEnd.next = l1
                break
            r2 = findEnd(l2,step)
            next_segment = r2.next

            r1.next = None
            r2.next = None
            start,end  = merge(l1, r1, l2, r2)
            lastTeamEnd.next = start
            lastTeamEnd = end
        step *= 2
    return head


def findEnd(head, step):
    cur = head
    while step > 1 and cur.next:
        cur = cur.next
        step -= 1
    return cur


def merge(l1, r1, l2, r2):
    if l1.val <= l2.val:
        start = l1
        pre = l1
        l1 = l1.next
    else:
        start = l2
        pre = l2
        l2 = l2.next

    while l1 and l2 :
        if l1.val <= l2.val:
            pre.next = l1
            pre = l1
            l1 = l1.next
        else:
            pre.next = l2
            pre = l2
            l2 = l2.next

    if l1:
        pre.next = l1
        end = r1
    else:
        pre.next = l2
        end = r2

    # pre = end
    # pre.next = None

    return start, end 


#-----------------------------------------------------------------------------

def main():

    ListNode1 = ListNode(1)
    ListNode2 = ListNode(3)
    ListNode3 = ListNode(2)
    ListNode4 = ListNode(4)
    ListNode1.next = ListNode2
    ListNode2.next = ListNode3
    ListNode3.next = ListNode4

    # ListNode1 = ListNode(-1)
    # ListNode2 = ListNode(5)
    # ListNode3 = ListNode(3)
    # ListNode4 = ListNode(4)
    # ListNode5 = ListNode(0)
    # ListNode1.next = ListNode2
    # ListNode2.next = ListNode3
    # ListNode3.next = ListNode4
    # ListNode4.next = ListNode5

    head = sortList(ListNode1)

    cur = head 
    while cur:
        print(cur.val)
        cur = cur.next


if __name__ == "__main__":
    main()