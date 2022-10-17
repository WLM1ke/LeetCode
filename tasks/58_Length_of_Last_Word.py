# https://leetcode.com/problems/length-of-last-word/


class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        letter = None
        pos = len(s) - 1
        while pos >= 0:
            if letter is None:
                if s[pos] != " ":
                    letter = pos
            elif s[pos] == " ":
                break

            pos -= 1

        return letter - pos
