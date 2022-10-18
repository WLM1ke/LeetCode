# https://leetcode.com/problems/cut-off-trees-for-golf-event/solution/
import collections

from typing import List


class Solution:
    def cutOffTree(self, forest: List[List[int]]) -> int:
        trees = [val for row in forest for val in row if val > 1]
        trees.sort()

        count = 0
        x, y = 0, 0

        for tree in trees:
            x, y, steps = _traverse(forest, x, y, tree)
            if steps == -1:
                return -1

            count += steps

        return count


def _traverse(forest, x, y, value):
    max_x = len(forest) - 1
    max_y = len(forest[0]) - 1

    seen = set()
    seen.add((x, y))
    que = collections.deque()
    que.append((x, y, 0))

    while que:
        x, y, count = que.popleft()
        if forest[x][y] == value:
            return x, y, count

        for nx, ny in ((x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)):
            if (nx, ny) in seen or nx < 0 or nx > max_x or ny < 0 or ny > max_y or not forest[nx][ny]:
                continue

            seen.add((nx, ny))
            que.append((nx, ny, count + 1))

    return 0, 0, -1
