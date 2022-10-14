# https://leetcode.com/problems/search-in-rotated-sorted-array-ii/
from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        low, high = 0, len(nums) - 1

        while low < high:
            if nums[low] == nums[high]:
                low += 1

                continue

            mid = (low + high) >> 1

            if nums[mid] == target:
                return True

            if nums[mid] > nums[high]:
                if nums[low] <= target < nums[mid]:
                    high = mid - 1
                else:
                    low = mid + 1

            else:
                if nums[mid] < target <= nums[high]:
                    low = mid + 1
                else:
                    high = mid - 1

        return nums[high] == target
