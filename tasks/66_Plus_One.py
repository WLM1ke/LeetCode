# https://leetcode.com/problems/plus-one/
from typing import List


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        over = 1

        for pos in range(len(digits) - 1, -1, -1):
            over, digits[pos] = divmod(digits[pos] + over, 10)

            if not over:
                return digits

        return [over] + digits
