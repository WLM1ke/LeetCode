# https://leetcode.com/problems/flood-fill/
from typing import List


class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        rows = len(image)
        cols = len(image[0])

        base = image[sr][sc]
        if base == color:
            return image

        image[sr][sc] = color

        for nr, nc in ((sr - 1, sc), (sr + 1, sc), (sr, sc - 1), (sr, sc + 1)):
            if nr < 0 or nr >= rows or nc < 0 or nc >= cols or base != image[nr][nc]:
                continue

            self.floodFill(image, nr, nc, color)

        return image
