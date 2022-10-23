# https://leetcode.com/problems/longest-palindromic-substring/
class Solution:
    def longestPalindrome(self, s: str) -> str:
        best = ""
        size = 0

        for pos in range(len(s)):
            if is_poly(s[pos - size: pos + 1]):
                best = s[pos - size: pos + 1]
                size += 1

            if pos - size - 1 >= 0 and is_poly(s[pos - size - 1: pos + 1]):
                best = s[pos - size - 1: pos + 1]
                size += 2

        return best


def is_poly(s):
    for pos in range(len(s) >> 1):
        if s[pos] != s[~pos]:
            return False

    return True
