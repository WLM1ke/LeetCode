# https://leetcode.com/problems/sum-of-left-leaves/
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        return _traverse(root, False)


def _traverse(node, is_left):
    if node.left is None and node.right is None:
        if is_left:
            return node.val

        return 0

    return ((node.left or 0) and _traverse(node.left, True))
