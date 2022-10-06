# https://leetcode.com/problems/4sum/
from typing import List


class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        if len(nums) < 4:
            return []

        nums.sort()
        cache = {target - i: n for n, i in enumerate(nums)}

        rez = set()

        for first in range(0, len(nums) - 3):
            for second in range(first + 1, len(nums) - 2):
                for third in range(second + 1, len(nums) - 1):
                    s = nums[first] + nums[second] + nums[third]
                    last = cache.get(s, -1)
                    if last > third:
                        rez.add((nums[first], nums[second], nums[third], nums[last]))

        return rez
