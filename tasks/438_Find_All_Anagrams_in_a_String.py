# https://leetcode.com/problems/find-all-anagrams-in-a-string/
import collections
from typing import List


class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        target = collections.defaultdict(int)

        for lt in p:
            target[lt] += 1

        size = len(p)
        window = collections.defaultdict(int)
        rez = []

        for pos, lt in enumerate(s):
            window[lt] += 1
            if pos >= size:
                pr = s[pos - size]
                window[pr] -= 1
                if window[pr] == 0:
                    window.pop(pr)

            if window == target:
                rez.append(pos + 1 - size)

        return rez
