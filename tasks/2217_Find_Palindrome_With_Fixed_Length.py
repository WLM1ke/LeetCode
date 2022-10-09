# https://leetcode.com/problems/find-palindrome-with-fixed-length/
from typing import List


class Solution:
    def kthPalindrome(self, queries: List[int], intLength: int) -> List[int]:
        have_middle = intLength % 2

        l = intLength // 2 + have_middle

        min_n = 10 ** (l - 1)
        max_n = 10 ** l - 1
        count = max_n - min_n + 1

        rez = []

        for query in queries:
            if query > count:
                rez.append(-1)
                continue

            base = min_n + query - 1

            if not have_middle:
                rez.append(base * min_n * 10 + int(str(base)[::-1]))

                continue

            if l == 1:
                rez.append(base)

                continue

            rez.append(base * min_n + int(str(base)[-2::-1]))

        return rez
