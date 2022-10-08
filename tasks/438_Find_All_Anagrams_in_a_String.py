# https://leetcode.com/problems/find-all-anagrams-in-a-string/
from typing import List


class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        rez = []
        if len(p) > len(s):
            return rez

        dest = {}
        for let in p:
            dest[let] = dest.get(let, 0) + 1

        source = {}

        for i in range(len(p)):
            let = s[i]
            source[let] = source.get(let, 0) + 1

        if dest == source:
            rez.append(0)

        delta = len(p)
        for i in range(len(s) - delta):
            source[s[i]] -= 1
            if source[s[i]] == 0:
                source.pop(s[i])
            source[s[i + delta]] = source.get(s[i + delta], 0) + 1

            if dest == source:
                rez.append(i + 1)

        return rez
