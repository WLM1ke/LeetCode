# https://leetcode.com/problems/length-of-last-word/


class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        first = None

        for pos, let in enumerate(reversed(s)):
            if first is None:
                if let != " ":
                    first = pos
            elif let == " ":
                return pos - first

        return len(s) - first
