# https://leetcode.com/problems/balanced-binary-tree/
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        return self.height(root) != -1

    def height(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0

        if (lh := self.height(root.left)) == -1 or (rh := self.height(root.right)) == -1:
            return -1

        if abs(lh - rh) <= 1:
            return max(lh, rh) + 1

        return -1
