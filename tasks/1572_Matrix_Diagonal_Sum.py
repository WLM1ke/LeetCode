# https://leetcode.com/problems/matrix-diagonal-sum/
from typing import List


class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        half = len(mat) >> 1

        rez = 0
        for i in range(half):
            rez += mat[i][i] + mat[~i][i] + mat[i][~i] + mat[~i][~i]

        if len(mat) % 2 == 1:
            rez += mat[half][half]

        return rez
