# https://leetcode.com/problems/flipping-an-image/
from typing import List


class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        for row in image:
            _row(row)

        return image


def _row(row):
    half = (len(row) + 1) >> 1

    for i in range(half):
        row[i], row[~i] = 1 ^ row[~i], 1 ^ row[i]
