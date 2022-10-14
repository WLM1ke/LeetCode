# https://leetcode.com/problems/remove-element/
from typing import List


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        pointer = -1
        for i in range(len(nums) - 1, -1, -1):
            if nums[i] == val:
                nums[i], nums[pointer] = nums[pointer], nums[i]
                pointer -= 1

        return len(nums) + 1 + pointer
