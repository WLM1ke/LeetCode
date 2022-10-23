# https://leetcode.com/problems/find-largest-value-in-each-tree-row/
import collections
from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        lvl = -1
        que = collections.deque()
        que.append((root, 0))
        rez = []

        while que:
            node, cur_lvl = que.popleft()

            if not node:
                continue

            if cur_lvl > lvl:
                lvl = cur_lvl
                rez.append(node.val)
            else:
                rez[-1] = max(rez[-1], node.val)

            que.append((node.left, cur_lvl + 1))
            que.append((node.right, cur_lvl + 1))

        return rez
