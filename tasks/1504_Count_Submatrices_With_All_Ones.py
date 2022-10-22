# https://leetcode.com/problems/count-submatrices-with-all-ones/
from typing import List


class Solution:
    def numSubmat(self, mat: List[List[int]]) -> int:

        count = 0

        for x, row in enumerate(mat):
            for y, val in enumerate(row):
                pre = 0
                if y > 0:
                    pre = row[y - 1]

                row[y] += pre * row[y]

                width = row[y]

                for xx in range(x, -1, -1):
                    width = min(width, mat[xx][y])
                    if width == 0:
                        break

                    count += width

        return count
