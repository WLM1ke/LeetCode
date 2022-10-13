# https://leetcode.com/problems/merge-intervals/
from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()

        start = intervals[0][0]
        end = intervals[0][1]

        rez = []

        for n in range(1, len(intervals)):
            start_next = intervals[n][0]
            end_next = intervals[n][1]
            if start_next > end:
                rez.append([start, end])
                start, end = start_next, end_next

                continue

            end = max(end, end_next)

        rez.append([start, end])

        return rez
