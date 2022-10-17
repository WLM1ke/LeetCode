# https://leetcode.com/problems/insufficient-nodes-in-root-to-leaf-paths/
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sufficientSubset(self, root: Optional[TreeNode], limit: int) -> Optional[TreeNode]:
        if root is None or not _traverse(0, root, limit):
            return None

        return root


def _traverse(cur, root, limit):
    cur = cur + root.val

    if root.left is None and root.right is None:
        return cur >= limit

    flag = False

    if root.left is not None:
        if not (left := _traverse(cur, root.left, limit)):
            root.left = None

        flag = flag or left

    if root.right is not None:
        if not (right := _traverse(cur, root.right, limit)):
            root.right = None

        flag = flag or right

    return flag
