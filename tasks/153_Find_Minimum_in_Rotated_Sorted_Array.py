# https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/
from typing import List


class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = -1, len(nums) - 1

        while l + 1 < r:
            mid = (l + r) >> 1

            if nums[mid] > nums[r]:
                l = mid
            else:
                r = mid

        return nums[r]
