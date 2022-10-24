# https://leetcode.com/problems/mean-of-array-after-removing-some-elements/
from typing import List


class Solution:
    def trimMean(self, arr: List[int]) -> float:
        arr.sort()
        trim = len(arr) // 20

        return sum(arr[trim:~trim + 1]) / (len(arr) - 2 * trim)
