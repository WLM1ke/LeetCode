# https://leetcode.com/problems/range-sum-query-2d-immutable/
from typing import List


class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.cumsum = [[0] * (len(matrix[0]) + 1) for _ in range(len(matrix) + 1)]

        for x, row in enumerate(matrix, 1):
            for y, val in enumerate(row, 1):
                self.cumsum[x][y] = val + self.cumsum[x - 1][y] + self.cumsum[x][y - 1] - self.cumsum[x - 1][y - 1]

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        return self.cumsum[row2 + 1][col2 + 1] + self.cumsum[row1][col1] - self.cumsum[row1][col2 + 1] - \
               self.cumsum[row2 + 1][col1]

# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)
