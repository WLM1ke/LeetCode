# https://leetcode.com/problems/longest-common-prefix/
from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        pre = strs[0]

        for i in range(1, len(strs)):
            pre = pre[:len(strs[i])]

            for n, (f, s) in enumerate(zip(pre, strs[i])):
                if f == s:
                    continue

                pre = pre[:n]
                break

            if not pre:
                return ""

        return pre
