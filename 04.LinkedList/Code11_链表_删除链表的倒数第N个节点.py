###########################################################################
# 删除链表的倒数第 N 个结点
#
# https://leetcode.cn/problems/remove-nth-node-from-end-of-list
###########################################################################

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if not head or not head.next:
            return None

        total_node = 0
        cur = head
        while cur:
            total_node +=1
            cur = cur.next

        new = ListNode()
        new.next = head

        pre = new
        cur = head
        for i in range(total_node - n):     
            pre = pre.next
            cur = cur.next
        pre.next = cur.next
        return new.next
        