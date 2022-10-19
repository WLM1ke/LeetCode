# https://leetcode.com/problems/number-of-closed-islands/

import collections

from typing import List


class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        bad = set()
        test = set()

        max_x = len(grid) - 1
        max_y = len(grid[0]) - 1

        for x, row in enumerate(grid):
            for y, val in enumerate(row):
                if val == 0:
                    if x == 0 or y == 0 or x == max_x or y == max_y:
                        bad.add((x, y))
                    else:
                        test.add((x, y))

        count = 0

        while test:
            que = collections.deque()
            que.append(test.pop())

            cur = set()
            cur.add(que[0])
            inner = True

            while que:
                x, y = que.popleft()

                for nx, ny in ((x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)):
                    if (nx, ny) in bad:
                        inner = False
                    elif (nx, ny) in test:
                        test.remove((nx, ny))
                        cur.add((nx, ny))
                        que.append((nx, ny))

            if inner:
                count += 1
                continue

            bad |= cur

        return count
