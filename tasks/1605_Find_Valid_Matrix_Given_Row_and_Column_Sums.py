# https://leetcode.com/problems/find-valid-matrix-given-row-and-column-sums/
from typing import List


class Solution:
    def restoreMatrix(self, rowSum: List[int], colSum: List[int]) -> List[List[int]]:
        mat = [[0] * len(colSum) for _ in rowSum]

        row = 0
        col = 0

        while row < len(rowSum) and col < len(colSum):
            val = min(rowSum[row], colSum[col])
            mat[row][col] = val

            rowSum[row] -= val
            if rowSum[row] == 0:
                row += 1

            colSum[col] -= val
            if colSum[col] == 0:
                col += 1

        return mat
