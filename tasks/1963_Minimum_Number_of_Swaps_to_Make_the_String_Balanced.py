# https://leetcode.com/problems/minimum-number-of-swaps-to-make-the-string-balanced/

class Solution:
    def minSwaps(self, s: str) -> int:
        swaps = 0
        last = len(s) - 1
        opened = 0

        for i in range(len(s)):
            if i == last:
                return swaps

            if s[i] == "[":
                opened += 1

                continue

            if opened > 0:
                opened -= 1

                continue

            swaps += 1
            opened += 1

            while s[last] != "[":
                last -= 1

            last -= 1

        return swaps
