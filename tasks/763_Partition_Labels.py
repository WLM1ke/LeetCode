# https://leetcode.com/problems/partition-labels/
from typing import List


class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        cache = {let: pos for pos, let in enumerate(s)}

        pre = -1
        end = -1
        rez = []

        for pos, let in enumerate(s):
            end = max(end, cache[let])

            if end == pos:
                rez.append(end - pre)
                pre = end

        return rez
