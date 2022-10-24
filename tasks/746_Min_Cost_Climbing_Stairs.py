# https://leetcode.com/problems/min-cost-climbing-stairs/
from typing import List


class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        prev2 = cost[0]
        prev1 = cost[1]

        for pos in range(2, len(cost)):
            prev2, prev1 = prev1, min(prev1, prev2) + cost[pos]

        return min(prev1, prev2)
