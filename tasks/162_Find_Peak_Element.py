# https://leetcode.com/problems/find-peak-element/
from typing import List


class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 0
        elif nums[0] > nums[1]:
            return 0
        elif nums[-1] > nums[-2]:
            return len(nums) - 1

        l = 0
        r = len(nums) - 1

        while l + 1 < r:
            m = (l + r) >> 1

            if nums[m] > nums[m - 1] and nums[m] > nums[m + 1]:
                return m

            if nums[m] > nums[m - 1]:
                l = m
            else:
                r = m
