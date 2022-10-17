# https://leetcode.com/problems/relative-sort-array/
from typing import List


class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        dif = len(arr2) * 2
        indexes = {num: pos - dif for pos, num in enumerate(arr2)}
        arr1.sort(key=lambda x: indexes.get(x, x))

        return arr1
