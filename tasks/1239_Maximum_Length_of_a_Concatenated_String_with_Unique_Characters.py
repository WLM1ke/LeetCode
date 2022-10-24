# https://leetcode.com/problems/maximum-length-of-a-concatenated-string-with-unique-characters/
from typing import List


class Solution:
    def maxLength(self, arr: List[str]) -> int:
        uniq = frozenset(s for word in arr if len(word) == len(s := frozenset(word)))

        rez = [frozenset()]

        for word in uniq:
            for pos in range(len(rez)):
                if not (rez[pos] & word):
                    rez.append(rez[pos] | word)
                    if len(rez[-1]) == 26:
                        return 26

        return max(map(len, rez))
