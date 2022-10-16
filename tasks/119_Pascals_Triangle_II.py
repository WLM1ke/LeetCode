# https://leetcode.com/problems/pascals-triangle-ii/
from typing import List


class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        row = []

        for _ in range(rowIndex + 1):
            prev = 0
            for pos in range(len(row)):
                prev, row[pos] = row[pos], row[pos] + prev

            row.append(1)

        return row
