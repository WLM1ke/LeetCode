# https://leetcode.com/problems/my-calendar-iii/
import bisect


class MyCalendarThree:

    def __init__(self):
        self._ends = []
        self._max_count = 0

    def book(self, start: int, end: int) -> int:
        ends = self._ends

        i = bisect.bisect_left(ends, start, key=lambda x: x[0])
        if i == len(ends):
            ends.append([start, 1])
            ends.append([end, 0])

            self._max_count = max(self._max_count, 1)

            return self._max_count

        if ends[i][0] != start:
            prev = 0
            if i != 0:
                prev = ends[i - 1][1]

            ends.insert(i, [start, prev + 1])
            self._max_count = max(self._max_count, prev + 1)

            i += 1

        while i < len(ends):
            if ends[i][0] < end:
                ends[i][1] += 1
                self._max_count = max(self._max_count, ends[i][1])
                i += 1
                continue

            if ends[i][0] == end:
                break

            if ends[i][0] > end:
                ends.insert(i, [end, ends[i - 1][1] - 1])
                break

        if i == len(ends):
            ends.append([end, 0])

        return self._max_count
