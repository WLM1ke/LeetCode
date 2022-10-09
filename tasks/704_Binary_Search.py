# https://leetcode.com/problems/binary-search/
from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = -1, len(nums)

        while l + 1 < r:
            mid = (l + r) // 2

            if nums[mid] > target:
                r = mid
            else:
                l = mid

        if l == -1 or nums[l] != target:
            return -1

        return l
