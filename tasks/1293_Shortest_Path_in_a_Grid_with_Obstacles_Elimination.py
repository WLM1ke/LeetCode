# https://leetcode.com/problems/shortest-path-in-a-grid-with-obstacles-elimination/
import collections
from typing import List


class Solution:
    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        visited = {(0, 0): k}
        que = collections.deque([(0, 0, k, 0)])

        mx = len(grid) - 1
        my = len(grid[0]) - 1

        while que:
            x, y, left, step = que.popleft()
            if x == mx and y == my:
                return step

            for xx, yy in ((x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)):
                if 0 <= xx <= mx and 0 <= yy <= my and (nl := left - grid[xx][yy]) > visited.get((xx, yy), -1):
                    visited[(xx, yy)] = nl
                    que.append((xx, yy, nl, step + 1))

        return -1
