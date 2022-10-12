# https://leetcode.com/problems/partition-labels/
from typing import List


class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        cache = {letter: n for n, letter in enumerate(s)}

        pre = -1
        last = 0
        rez = []

        for n, letter in enumerate(s):
            last = max(last, cache[letter])
            if last == n:
                rez.append(n - pre)
                pre = n
                last = n

        return rez
