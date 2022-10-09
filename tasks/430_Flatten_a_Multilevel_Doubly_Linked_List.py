# https://leetcode.com/problems/flatten-a-multilevel-doubly-linked-list/
from typing import Optional


class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child


class Solution:
    def flatten(self, head: Optional[Node]) -> Optional[Node]:
        self.traverse(head)

        return head

    def traverse(self, head: Optional[Node]) -> Optional[Node]:
        prev = None

        while head:
            prev = head
            if not head.child:
                head = head.next

                continue

            next_ = head.next
            child = head.child

            head.child = None
            head.next = child

            child.prev = head

            prev = self.traverse(child)

            prev.next = next_
            head = next_
            if head:
                head.prev = prev

        return prev
