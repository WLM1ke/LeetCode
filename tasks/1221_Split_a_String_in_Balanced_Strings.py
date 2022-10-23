# https://leetcode.com/problems/split-a-string-in-balanced-strings/

class Solution:
    def balancedStringSplit(self, s: str) -> int:
        balance = 0
        counter = 0

        mapper = {
            "R": 1,
            "L": -1,
        }

        for lt in s:
            balance += mapper[lt]

            if balance == 0:
                counter += 1

        return counter
