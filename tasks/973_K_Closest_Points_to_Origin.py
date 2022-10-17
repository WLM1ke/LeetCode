# https://leetcode.com/problems/k-closest-points-to-origin/
import heapq

from typing import List


class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []

        for x, y in points:
            dist = -(x ** 2 + y ** 2)
            if len(heap) == k:
                heapq.heappushpop(heap, (dist, [x, y]))
            else:
                heapq.heappush(heap, (dist, [x, y]))

        return [point for _, point in heap]
