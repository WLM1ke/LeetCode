# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-transaction-fee/
from typing import List


class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        min_pr, max_pr = prices[0], prices[0]

        profit = 0
        for n in range(1, len(prices)):
            cur = prices[n]

            if cur > max_pr:
                max_pr = cur

                continue

            if cur < max_pr - fee:
                profit += max(0, max_pr - min_pr - fee)

                min_pr, max_pr = cur, cur

                continue

            if cur < min_pr:
                min_pr, max_pr = cur, cur

        profit += max(0, max_pr - min_pr - fee)

        return profit
