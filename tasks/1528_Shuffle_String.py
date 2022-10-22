# https://leetcode.com/problems/shuffle-string/
from typing import List


class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        rez = [None] * len(s)

        for pos, ind in enumerate(indices):
            rez[ind] = s[pos]

        return "".join(rez)
