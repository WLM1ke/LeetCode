# https://leetcode.com/problems/search-a-2d-matrix/
from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix or not matrix[0]:
            return False

        rows = len(matrix)
        cols = len(matrix[0])

        l, r = -1, rows * cols - 1

        while l + 1 < r:
            mid = (l + r) >> 1
            row, col = divmod(mid, cols)

            if matrix[row][col] < target:
                l = mid
            else:
                r = mid

        row, col = divmod(r, cols)

        return matrix[row][col] == target
