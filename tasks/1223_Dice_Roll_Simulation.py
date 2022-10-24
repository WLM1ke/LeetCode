# https://leetcode.com/problems/dice-roll-simulation/
import collections
from typing import List

_MOD = 10 ** 9 + 7


class Solution:
    def dieSimulator(self, n: int, rollMax: List[int]) -> int:
        cache = collections.defaultdict(int)
        for i in range(6):
            cache[(i, 1)] = 1

        for _ in range(1, n):
            new_cache = collections.defaultdict(int)

            for (num, consecutive), count in cache.items():
                count %= _MOD

                for i in range(6):
                    if i != num:
                        new_cache[(i, 1)] += count
                    elif consecutive < rollMax[i]:
                        new_cache[(i, consecutive + 1)] += count

            cache = new_cache

        return sum(cache.values()) % _MOD
