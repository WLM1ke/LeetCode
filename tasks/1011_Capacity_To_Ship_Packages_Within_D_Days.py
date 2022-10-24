# https://leetcode.com/problems/capacity-to-ship-packages-within-d-days/
from typing import List


class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        start = max(weights) - 1
        end = sum(weights)

        while start + 1 < end:
            mid = (start + end) >> 1

            if _day_count(weights, mid) > days:
                start = mid
            else:
                end = mid

        return end


def _day_count(weights, cargo):
    count = 0

    left = 0
    for w in weights:
        if w > left:
            count += 1
            left = cargo

        left -= w

    return count
