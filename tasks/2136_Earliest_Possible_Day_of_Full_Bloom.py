# https://leetcode.com/problems/earliest-possible-day-of-full-bloom/
from typing import List


class Solution:
    def earliestFullBloom(self, plantTime: List[int], growTime: List[int]) -> int:
        rez = 0
        plant = 0

        for pl, gr in sorted(zip(plantTime, growTime), key=lambda x: (-x[1], x[0])):
            rez = max(rez, plant + pl + gr)
            plant += pl

        return rez
