# https://leetcode.com/problems/product-of-array-except-self/
from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        rez = [1] * len(nums)
        rez[len(nums) - 1] = 1
        for pos in range(len(nums) - 2, -1, -1):
            rez[pos] = rez[pos + 1] * nums[pos + 1]

        prev = 1
        for pos in range(len(nums)):
            rez[pos] *= prev
            prev *= nums[pos]

        return rez
