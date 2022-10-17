# https://leetcode.com/problems/path-sum-ii/
from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        if root is None:
            return []

        rez = []
        _traverse(rez, [], root, targetSum)

        return rez


def _traverse(rez, cur, root, targetSum):
    if root.left is None and root.right is None:
        if sum(cur) + root.val == targetSum:
            rez.append(cur + [root.val])

        return

    cur.append(root.val)

    if root.left is not None:
        _traverse(rez, cur, root.left, targetSum)

    if root.right is not None:
        _traverse(rez, cur, root.right, targetSum)

    cur.pop()
