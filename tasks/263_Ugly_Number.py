# https://leetcode.com/problems/ugly-number/
class Solution:
    def isUgly(self, n: int) -> bool:
        if n <= 0:
            return False

        for div in (2, 3, 5):
            while True:
                nn, rem = divmod(n, div)
                if rem != 0:
                    break

                n = nn

        return n == 1
