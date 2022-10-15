# https://leetcode.com/problems/length-of-last-word/


class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        last_space = -1
        has_letter = False
        for pos, let in enumerate(reversed(s)):
            if let == " " and not has_letter:
                last_space = pos
            elif let == " ":
                return pos - last_space - 1
            else:
                has_letter = True

        return len(s) - last_space - 1
