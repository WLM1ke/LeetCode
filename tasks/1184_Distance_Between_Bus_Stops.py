# https://leetcode.com/problems/distance-between-bus-stops/
from typing import List


class Solution:
    def distanceBetweenBusStops(self, distance: List[int], start: int, destination: int) -> int:
        start_dist = 0
        destination_dist = 0
        all_dist = 0

        for n, dist in enumerate(distance):
            if n == start:
                start_dist = all_dist

            if n == destination:
                destination_dist = all_dist

            all_dist += dist

        one_dir = abs(destination_dist - start_dist)

        return min(one_dir, all_dist - one_dir)
