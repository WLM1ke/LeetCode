# https://leetcode.com/problems/two-sum/
from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        cache = {}

        for pos, num in enumerate(nums):
            if (pos2 := cache.get(target - num)) is not None:
                return [pos2, pos]

            cache[num] = pos
