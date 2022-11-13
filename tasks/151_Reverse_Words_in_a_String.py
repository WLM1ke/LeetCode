# https://leetcode.com/problems/reverse-words-in-a-string/


class Solution:
    def reverseWords(self, s: str) -> str:
        return " ".join(reversed([w for w in s.split(" ") if w]))
