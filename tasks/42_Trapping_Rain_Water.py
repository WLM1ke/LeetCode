# https://leetcode.com/problems/trapping-rain-water/
from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        size = len(height)

        l = [0] * size
        r = [0] * size

        prev_l = 0
        prev_r = 0
        for n, h in enumerate(height):
            prev_l = max(prev_l, h)
            l[n] = prev_l

            prev_r = max(prev_r, height[size - 1 - n])
            r[size - 1 - n] = prev_r

        vol = 0
        for h, lh, rh in zip(height, l, r):
            vol += min(lh, rh) - h

        return vol
