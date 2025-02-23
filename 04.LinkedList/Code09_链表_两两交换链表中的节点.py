###########################################################################
# 两两交换链表中的节点
#
# https://leetcode.cn/problems/swap-nodes-in-pairs
###########################################################################


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head

        dummyHead = ListNode()
        dummyHead.next = head
        cur = dummyHead

        while cur.next and cur.next.next:
            a, b = cur.next, cur.next.next
            cur.next = b
            a.next = b.next
            b.next = a
            cur = a
        return dummyHead.next