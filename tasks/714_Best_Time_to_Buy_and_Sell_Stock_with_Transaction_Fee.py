# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-transaction-fee/
from typing import List


class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        have = -prices[0]
        not_have = 0

        for n in range(1, len(prices)):
            have, not_have = max(have, not_have - prices[n]), max(not_have, prices[n] + have - fee)

        return not_have
