# https://leetcode.com/problems/longest-palindromic-substring/
class Solution:
    def longestPalindrome(self, s: str) -> str:
        best = ""

        for pos in range(len(s)):
            start = pos - len(best)
            cur = s[start:pos + 1]
            if cur == cur[::-1]:
                best = cur

            if start > 0:
                start -= 1
                cur = s[start:pos + 1]
                if cur == cur[::-1]:
                    best = cur

        return best
