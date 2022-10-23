# https://leetcode.com/problems/number-of-closed-islands/
from typing import List


class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        count = 0

        for x, row in enumerate(grid):
            for y, val in enumerate(row):
                if not grid[x][y]:
                    grid[x][y] = 1
                    count += _traverse(grid, x, y)

        return count


def _traverse(grid, x, y):
    max_x = len(grid) - 1
    max_y = len(grid[0]) - 1

    flag = x != 0 and x != max_x and y != 0 and y != max_y

    for xx, yy in ((x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)):
        if (0 <= xx <= max_x) and (0 <= yy <= max_y) and not grid[xx][yy]:
            grid[xx][yy] = 1
            flag &= _traverse(grid, xx, yy)

    return flag
