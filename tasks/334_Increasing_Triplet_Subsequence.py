# https://leetcode.com/problems/increasing-triplet-subsequence/
from typing import List


class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        pre = None

        first_pre = 2 ** 31
        first = 2 ** 31
        second = 2 ** 31

        for i in range(len(nums)):
            cur = nums[i]

            if second < cur:
                return True

            if first < cur < second:
                second = cur

            if cur < first_pre:
                first_pre = cur

            if first_pre < cur < second:
                first = first_pre
                second = cur
                first_pre = 2 ** 31

        return False
