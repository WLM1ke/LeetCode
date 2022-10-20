# https://leetcode.com/problems/leaf-similar-trees/
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        try:
            for val1, val2 in zip(_traverse(root1), _traverse(root2), strict=True):
                if val1 != val2:
                    return False
        except:
            return False

        return True


def _traverse(root):
    if root.left is None and root.right is None:
        yield root.val

        return

    if root.left is not None:
        yield from _traverse(root.left)

    if root.right is not None:
        yield from _traverse(root.right)
