# https://leetcode.com/problems/reverse-integer/

class Solution:
    def reverse(self, x: int) -> int:
        sign = [1, -1][x < 0]

        rez = 0

        while x > 0:
            x, ost = divmod(x, 10)

            rez = rez * 10 + ost

        rez *= sign

        if rez < -(2 ** 31) or rez > 2 ** 31 - 1:
            rez = 0

        return rez
