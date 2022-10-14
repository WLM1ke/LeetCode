# https://leetcode.com/problems/delete-the-middle-node-of-a-linked-list/
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        root = head
        count = 0

        while head:
            count += 1
            head = head.next

        head = root
        count >>= 1

        if not count:
            return head.next

        while count > 1:
            head = head.next
            count -= 1

        head.next = head.next.next

        return root
