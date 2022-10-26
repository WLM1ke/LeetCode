# https://leetcode.com/problems/duplicate-zeros/
from typing import List


class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        zeros = 0
        pointer = len(arr) - 1

        for end, num in enumerate(arr):
            if num == 0:
                zeros += 1

            if end + zeros == len(arr) - 1:
                break

            if end + zeros == len(arr):
                arr[-1] = 0
                end -= 1
                pointer -= 1

                break

        for pos in range(end, -1, -1):
            num = arr[pos]

            arr[pointer] = num
            pointer -= 1

            if num == 0:
                arr[pointer] = 0
                pointer -= 1
