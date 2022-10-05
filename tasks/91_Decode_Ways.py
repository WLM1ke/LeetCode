from functools import lru_cache


class Solution:
    @lru_cache
    def numDecodings(self, s: str) -> int:
        if not s:
            return 1

        if s[0] == "0":
            return 0

        if len(s) == 1:
            return 1

        if s[0] == "1" or (s[0] == "2" and s[1] <= "6"):
            return self.numDecodings(s[1:]) + self.numDecodings(s[2:])

        return self.numDecodings(s[1:])