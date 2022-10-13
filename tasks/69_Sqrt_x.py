# https://leetcode.com/problems/sqrtx/

class Solution:
    def mySqrt(self, x: int) -> int:
        if x <= 1:
            return x

        l, r = 0, x

        while l + 1 < r:
            mid = (r + l) >> 1

            if mid ** 2 > x:
                r = mid
            else:
                l = mid

        return l
