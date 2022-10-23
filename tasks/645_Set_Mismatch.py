# https://leetcode.com/problems/set-mismatch/
from typing import List


class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:

        dub = None
        miss = None

        for pos in range(len(nums)):
            num = abs(nums[pos])
            if nums[num - 1] < 0:
                dub = num
            else:
                nums[num - 1] *= -1

        for pos in range(len(nums)):
            if nums[pos] > 0:
                miss = pos + 1

        return [dub, miss]
