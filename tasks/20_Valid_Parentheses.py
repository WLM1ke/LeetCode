# https://leetcode.com/problems/valid-parentheses/

class Solution:
    def isValid(self, s: str) -> bool:
        mapper = {
            "}": "{",
            "]": "[",
            ")": "(",
        }

        stack = []

        for br in s:
            if (br_open := mapper.get(br)) is None:
                stack.append(br)
            elif not stack or stack.pop() != br_open:
                return False

        return not stack
