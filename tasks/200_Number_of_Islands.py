# https://leetcode.com/problems/number-of-islands/
from typing import List


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        count = 0

        for x, row in enumerate(grid):
            for y, val in enumerate(row):
                if val == "1":
                    grid[x][y] = "0"
                    count += 1
                    _traverse(grid, x, y)

        return count


def _traverse(grid, x, y):
    for xx, yy in ((x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)):
        if 0 <= xx < len(grid) and 0 <= yy < len(grid[0]) and grid[xx][yy] == "1":
            grid[xx][yy] = "0"
            _traverse(grid, xx, yy)
