# https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree/
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        return create_sub_tree(nums, 0, len(nums) - 1)


def create_sub_tree(nums: List[int], start: int, end: int) -> Optional[TreeNode]:
    if end < start:
        return None

    half = (start + end) >> 1

    return TreeNode(nums[half], create_sub_tree(nums, start, half - 1), create_sub_tree(nums, half + 1, end))
