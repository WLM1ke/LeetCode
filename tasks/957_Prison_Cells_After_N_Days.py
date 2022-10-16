# https://leetcode.com/problems/prison-cells-after-n-days/
from typing import List


class Solution:
    def prisonAfterNDays(self, cells: List[int], n: int) -> List[int]:
        num = 0
        for cell in cells:
            num *= 2
            num += cell

        num = (0b11111111 - (num >> 1 ^ num << 1)) & 0b01111110
        origin = num

        for count in range(1, n):
            num = (0b11111111 - (num >> 1 ^ num << 1)) & 0b01111110
            if origin == num:
                n = (n - 1) % count
                for _ in range(0, n):
                    num = (0b11111111 - (num >> 1 ^ num << 1)) & 0b01111110

                break

        rez = [int(let) for let in str(bin(num))[2:]]

        return [0] * (8 - len(rez)) + rez
