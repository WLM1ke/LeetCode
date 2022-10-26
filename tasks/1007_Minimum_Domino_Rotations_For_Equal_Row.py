# https://leetcode.com/problems/minimum-domino-rotations-for-equal-row/
from typing import List


class Solution:
    def minDominoRotations(self, tops: List[int], bottoms: List[int]) -> int:
        t = 0
        b = 0
        same = 0

        nt = tops[0]
        nb = bottoms[0]

        for pos in range(1, len(tops)):
            if nt != tops[pos] and nt != bottoms[pos]:
                t = None
            elif nt == tops[pos]:
                pass
            elif t is not None:
                t += 1

            if nb != tops[pos] and nb != bottoms[pos]:
                b = None
            elif nb == bottoms[pos]:
                pass
            elif b is not None:
                b += 1

            if t is None and b is None:
                return -1

            if tops[pos] == bottoms[pos]:
                same += 1

        rez = len(tops)

        if t is not None:
            rez = min(rez, t, len(tops) - t - same)

        if b is not None:
            rez = min(rez, b, len(tops) - b - same)

        return rez
