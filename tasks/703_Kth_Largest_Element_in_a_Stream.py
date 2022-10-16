# https://leetcode.com/problems/kth-largest-element-in-a-stream/
import heapq

from typing import List


class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self._largest = []
        self._k = k

        for num in nums:
            self.add(num)

    def add(self, val: int) -> int:
        if len(self._largest) < self._k:
            heapq.heappush(self._largest, val)
        elif val > self._largest[0]:
            heapq.heappushpop(self._largest, val)

        return self._largest[0]

# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)
