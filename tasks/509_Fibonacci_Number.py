# https://leetcode.com/problems/fibonacci-number/

class Solution:
    def fib(self, n: int) -> int:
        if n == 0:
            return 0

        if n == 1:
            return 1

        a, b = 0, 1

        for _ in range(2, n + 1):
            a, b = b, b + a

        return b
