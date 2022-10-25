# https://leetcode.com/problems/repeated-substring-pattern/
class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        size = len(s)
        for pos, lt in enumerate(s, 1):

            if s[-1] != lt:
                continue

            count, rem = divmod(size, pos)

            if rem:
                continue

            if pos != size and s[:pos] * count == s:
                return True

        return False
