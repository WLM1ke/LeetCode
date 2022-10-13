# https://leetcode.com/problems/powx-n/

class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n < 0:
            return 1 / self.myPow(x, -n)

        if not n:
            return 1

        half_n, rem = divmod(n, 2)

        rez = self.myPow(x, half_n)

        rez *= rez

        if rem:
            rez *= x

        return rez
