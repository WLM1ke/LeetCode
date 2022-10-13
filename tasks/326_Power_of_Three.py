# https://leetcode.com/problems/power-of-three/

class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n < 1:
            return False

        while n > 1:
            n, rem = divmod(n, 3)
            if rem:
                return False

        return True
