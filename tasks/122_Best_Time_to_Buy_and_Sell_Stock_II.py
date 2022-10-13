# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/
from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        return sum(max(0, prices[n + 1] - prices[n]) for n in range(len(prices) - 1))
