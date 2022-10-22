# https://leetcode.com/problems/minimum-time-visiting-all-points/
from typing import List


class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        return sum(_time(points[i], points[i + 1]) for i in range(0, len(points) - 1))


def _time(p1, p2):
    xd = abs(p1[0] - p2[0])
    yd = abs(p1[1] - p2[1])

    return max(xd, yd)
