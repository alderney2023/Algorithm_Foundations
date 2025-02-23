###########################################################################
# 两数相加
#
# https://leetcode.cn/problems/add-two-numbers
###########################################################################


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:


        t = 0
        head = ListNode()
        pre = None
        while l1 or l2:
            x = ( (l1.val if l1 else 0) + (l2.val if l2 else 0) + t )
            cur = ListNode()
            cur.val = x%10
            t = x//10
            
            cur.next = pre
            pre = cur
            
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        
        if t :
            cur = ListNode()
            cur.val = 1
            cur.next = pre

        tail = cur
        pre = None
        while cur:
            next = cur.next
            cur.next = pre
            pre = cur
            cur = next 

        return pre