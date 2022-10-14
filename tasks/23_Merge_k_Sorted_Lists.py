# https://leetcode.com/problems/merge-k-sorted-lists/
import heapq

from typing import List, Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        match lists:
            case []:
                return None
            case [list1]:
                return list1
            case [list1, list2]:
                return self.merge(list1, list2)
            case _:
                half = len(lists) // 2
                return self.mergeKLists([self.mergeKLists(lists[:half]), self.mergeKLists(lists[half:])])

    def merge(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        root = ListNode()
        cur = root

        while list1 and list2:
            if list1.val < list2.val:
                cur.next, cur, list1 = list1, list1, list1.next
            else:
                cur.next, cur, list2 = list2, list2, list2.next

        if list1:
            cur.next = list1

        if list2:
            cur.next = list2

        return root.next


class SolutionHeap:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        root = cur = ListNode()

        heap = []

        for n, node in enumerate(lists):
            if node:
                heapq.heappush(heap, (node.val, n))

        while heap:
            _, n = heapq.heappop(heap)
            node = lists[n]

            cur.next = node
            cur = node

            if node.next:
                heapq.heappush(heap, (node.next.val, n))
                lists[n] = node.next

        return root.next
