# https://leetcode.com/problems/single-number/
class Solution:
    def singleNumber(self, nums: list[int]) -> int:
        count = 0
        for num in nums:
            count ^= num

        return count
