# https://leetcode.com/problems/minimum-operations-to-reduce-x-to-zero/
from typing import List


class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        if (target := sum(nums) - x) < 0:
            return -1
        elif target == 0:
            return len(nums)

        window = 0
        size = 0
        best = -1

        for pos, num in enumerate(nums):
            window += num
            size += 1

            while window > target:
                size -= 1
                window -= nums[pos - size]

            if window == target:
                best = max(best, size)

        if best == -1:
            return -1

        return len(nums) - best
