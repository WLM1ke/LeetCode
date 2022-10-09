# https://leetcode.com/problems/peak-index-in-a-mountain-array/
from typing import List


class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:

        l, r = 0, len(arr) - 1

        while l + 2 < r:
            mid = (l + r) // 2

            if arr[mid - 1] < arr[mid] and arr[mid] > arr[mid + 1]:
                return mid
            elif arr[mid - 1] < arr[mid]:
                l = mid
            else:
                r = mid

        return l + 1
