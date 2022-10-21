# https://leetcode.com/problems/minimum-depth-of-binary-tree/
import collections
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0

        que = collections.deque([(1, root)])

        while True:
            lvl, node = que.popleft()
            if node.left is None and node.right is None:
                return lvl

            if node.left:
                que.append((lvl + 1, node.left))

            if node.right:
                que.append((lvl + 1, node.right))
