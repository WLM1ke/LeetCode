# https://leetcode.com/problems/number-of-dice-rolls-with-target-sum/

import collections

_MOD = 10 ** 9 + 7


class Solution:
    def numRollsToTarget(self, n: int, k: int, target: int) -> int:
        que = collections.OrderedDict({(n, target): 1})

        while que:
            (left_n, left_target), rez = que.popitem(False)

            if left_target < left_n or left_target > left_n * k:
                continue

            if left_n == 0:
                return rez

            for i in range(1, k + 1):
                que[(left_n - 1, left_target - i)] = (que.get((left_n - 1, left_target - i), 0) + rez) % _MOD

        return 0
