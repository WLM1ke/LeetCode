# https://leetcode.com/problems/add-two-numbers/
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        pre_root = ListNode()
        cur = pre_root
        from_pre = 0

        while l1 or l2 or from_pre:
            val = ((l1 and l1.val) or 0) + ((l2 and l2.val) or 0) + from_pre

            cur.next = ListNode(val % 10)
            cur = cur.next

            from_pre = val // 10

            l1 = l1 and l1.next
            l2 = l2 and l2.next

        return pre_root.next or ListNode()
