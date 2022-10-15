# https://leetcode.com/problems/ugly-number-ii/


class Solution:
    def nthUglyNumber(self, n: int) -> int:
        ugly = [1]
        p2 = 0
        p3 = 0
        p5 = 0

        while len(ugly) < n:
            n2 = ugly[p2] * 2
            n3 = ugly[p3] * 3
            n5 = ugly[p5] * 5

            n_next = min(n2, n3, n5)
            ugly.append(n_next)

            if n2 == n_next:
                p2 += 1

            if n3 == n_next:
                p3 += 1

            if n5 == n_next:
                p5 += 1

        return ugly[-1]
