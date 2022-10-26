# https://leetcode.com/problems/continuous-subarray-sum/
from typing import List


class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        rem = {0: -1}
        cur = 0
        for pos, num in enumerate(nums):
            cur = (cur + num) % k
            if (old_pos := rem.get(cur)) is None:
                rem[cur] = pos
            elif pos - old_pos >= 2:
                return True

        return False
