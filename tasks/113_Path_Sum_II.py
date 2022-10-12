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

        return self.traverse(root, [], targetSum)

    def traverse(self, root: TreeNode, path: List[int], targetSum: int) -> List[List[int]]:
        path = path + [root.val]

        if (not (root.left or root.right)) and sum(path) == targetSum:
            return [path]

        rez = []
        if root.left:
            rez.extend(self.traverse(root.left, path, targetSum))

        if root.right:
            rez.extend(self.traverse(root.right, path, targetSum))

        return rez
