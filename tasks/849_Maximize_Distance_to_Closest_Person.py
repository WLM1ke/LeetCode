# https://leetcode.com/problems/maximize-distance-to-closest-person/
from typing import List


class Solution:
    def maxDistToClosest(self, seats: List[int]) -> int:
        dist = -1
        empty = 0

        for pos, val in enumerate(seats):
            if not val:
                empty += 1
            elif dist == -1:
                dist = max(dist, empty)
                empty = 0
            else:
                dist = max(dist, (empty + 1) // 2)
                empty = 0

        return max(dist, empty)
