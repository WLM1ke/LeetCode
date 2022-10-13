# https://leetcode.com/problems/remove-duplicates-from-sorted-array/
from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        pointer = 1

        for n in range(1, len(nums)):
            if nums[n] != nums[n - 1]:
                nums[pointer] = nums[n]
                pointer += 1

        return pointer
