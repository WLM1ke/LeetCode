# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_pr = prices[0]
        profit = 0

        for pr in prices:
            min_pr = min(min_pr, pr)
            profit = max(profit, pr - min_pr)

        return profit
