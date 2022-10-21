# https://leetcode.com/problems/contains-duplicate-ii/
from typing import List


class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        cache = {}

        for pos, num in enumerate(nums):
            if (pos_pre := cache.get(num)) is not None:
                if pos - pos_pre <= k:
                    return True

            cache[num] = pos

        return False
