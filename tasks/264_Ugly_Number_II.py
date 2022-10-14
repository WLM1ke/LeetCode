# https://leetcode.com/problems/ugly-number-ii/
import heapq


class Solution:
    def nthUglyNumber(self, n: int) -> int:
        nums = []
        heapq.heappush(nums, 1)

        rez = None

        for _ in range(n):
            rez = heapq.heappop(nums)
            while nums and rez == nums[0]:
                heapq.heappop(nums)

            heapq.heappush(nums, rez * 2)
            heapq.heappush(nums, rez * 3)
            heapq.heappush(nums, rez * 5)

        return rez
