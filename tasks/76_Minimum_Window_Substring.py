# https://leetcode.com/problems/minimum-window-substring/
import collections


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        best = " " * (len(s) + 1)

        target = collections.Counter(t)

        window = collections.Counter()
        size = 0

        for pos, lt in enumerate(s):
            size += 1
            if lt not in target:
                continue

            window[lt] = window.get(lt, 0) + 1

            while True:
                first_lt = s[pos + 1 - size]
                if first_lt not in target:
                    size -= 1
                    continue

                if window.get(first_lt, 0) > target[first_lt]:
                    size -= 1
                    window[first_lt] -= 1
                else:
                    break

            if target <= window and len(best) > size:
                best = s[pos + 1 - size: pos + 1]

        if len(best) == len(s) + 1:
            return ""

        return best
