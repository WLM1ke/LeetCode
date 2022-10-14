# https://leetcode.com/problems/move-zeroes/
from typing import List


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        pointer = 0

        for pos in range(len(nums)):
            if nums[pos] != 0:
                nums[pos], nums[pointer] = nums[pointer], nums[pos]
                pointer += 1
