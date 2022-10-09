# https://leetcode.com/problems/two-sum-iv-input-is-a-bst/
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def __init__(self):
        self._cache = set()

    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        return self.traverse_tree(root, k)

    def traverse_tree(self, root: Optional[TreeNode], target: int) -> bool:
        if root is None:
            return False

        if target - root.val in self._cache:
            return True

        self._cache.add(root.val)

        return self.traverse_tree(root.left, target) or self.traverse_tree(root.right, target)
