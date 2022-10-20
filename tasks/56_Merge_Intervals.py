# https://leetcode.com/problems/merge-intervals/
from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()

        start = intervals[0][0]
        end = intervals[0][0]
        rez = []

        for l, r in intervals:
            if l <= end:
                end = max(end, r)
            else:
                rez.append([start, end])
                start, end = l, r

        rez.append([start, end])

        return rez
