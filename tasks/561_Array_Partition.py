# https://leetcode.com/problems/array-partition/
from typing import List


class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        nums.sort()
        rez = 0

        for pos in range(0, len(nums), 2):
            rez += nums[pos]

        return rez
