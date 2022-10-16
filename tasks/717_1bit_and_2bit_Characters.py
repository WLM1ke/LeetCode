# https://leetcode.com/problems/1-bit-and-2-bit-characters/
from typing import List


class Solution:
    def isOneBitCharacter(self, bits: List[int]) -> bool:
        if len(bits) == 1:
            return True

        if bits[-2] == 0:
            return True

        count = 1

        for pos in range(-3, -len(bits) - 1, -1):
            if bits[pos] == 1:
                count += 1
            else:
                break

        return count % 2 == 0
