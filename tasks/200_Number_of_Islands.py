# https://leetcode.com/problems/number-of-islands/
from typing import List


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        count = 0

        for n, row in enumerate(grid):
            for k, mark in enumerate(row):
                count += self.remove_island(grid, n, k)

        return count

    def remove_island(self, grid: List[List[str]], n: int, k: int) -> int:
        if grid[n][k] == "0":
            return 0

        grid[n][k] = "0"

        if n > 0:
            self.remove_island(grid, n - 1, k)

        if n < len(grid) - 1:
            self.remove_island(grid, n + 1, k)

        if k > 0:
            self.remove_island(grid, n, k - 1)

        if k < len(grid[0]) - 1:
            self.remove_island(grid, n, k + 1)

        return 1
