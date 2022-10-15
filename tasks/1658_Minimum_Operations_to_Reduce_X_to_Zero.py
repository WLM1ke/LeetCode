# https://leetcode.com/problems/minimum-operations-to-reduce-x-to-zero/
from typing import List


class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        min_ops = 10 ** 6
        cache = {}
        running = 0

        for pos, num in enumerate(nums, 1):
            running += num

            if running == x:
                min_ops = pos

                break

            if running > x:
                break

            cache[running] = pos

        if running < x:
            return -1

        running = 0

        for pos, num in enumerate(reversed(nums), 1):
            running += num

            if running == x:
                return min(min_ops, pos)

            if running > x:
                break

            if (pos_left := cache.get(x - running)) is not None:
                if pos_left + pos > len(nums):
                    continue

                min_ops = min(min_ops, pos_left + pos)

        if min_ops == 10 ** 6:
            return -1

        return min_ops
