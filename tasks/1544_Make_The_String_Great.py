# https://leetcode.com/problems/make-the-string-great/
class Solution:
    def makeGood(self, s: str) -> str:
        start = 0

        while start < len(s) - 1:
            if ((s[start].islower() and s[start].upper() == s[start + 1])
                    or (s[start].isupper() and s[start].lower() == s[start + 1])
            ):
                s = s[:start] + s[start + 2:]
                start = max(0, start - 1)
            else:
                start += 1

        return s
