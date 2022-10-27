# https://leetcode.com/problems/fruit-into-baskets/
import collections
from typing import List


class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        best = 0
        basket = collections.defaultdict(int)

        for pos, fruit in enumerate(fruits):
            basket[fruit] += 1

            while len(basket) > 2:
                delta = sum(basket.values())
                prev_fruit = fruits[pos + 1 - delta]

                basket[prev_fruit] -= 1
                if basket[prev_fruit] == 0:
                    basket.pop(prev_fruit)

            best = max(best, sum(basket.values()))

        return best
