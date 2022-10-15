# https://leetcode.com/problems/distance-between-bus-stops/
from typing import List


class Solution:
    def distanceBetweenBusStops(self, distance: List[int], start: int, destination: int) -> int:
        full = sum(distance)
        if start > destination:
            start, destination = destination, start

        forward = sum(distance[start:destination])

        return min(full - forward, forward)
