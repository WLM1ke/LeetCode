# https://leetcode.com/problems/find-median-from-data-stream/

import heapq


class MedianFinder:

    def __init__(self):
        self._upper = []
        self._lower = []

    def addNum(self, num: int) -> None:
        if len(self._upper) == len(self._lower):
            if not self._lower or (num >= -self._lower[0]):
                heapq.heappush(self._upper, num)
            else:
                heapq.heappush(self._upper, -heapq.heappushpop(self._lower, -num))
        else:
            if num <= -self._upper[0]:
                heapq.heappush(self._lower, -num)
            else:
                heapq.heappush(self._lower, -heapq.heappushpop(self._upper, num))

    def findMedian(self) -> float:
        if len(self._upper) == len(self._lower):
            return (self._upper[0] - self._lower[0]) / 2
        else:
            return self._upper[0]
