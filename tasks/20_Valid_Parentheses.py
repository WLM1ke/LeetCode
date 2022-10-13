# https://leetcode.com/problems/valid-parentheses/

class Solution:
    def isValid(self, s: str) -> bool:
        mapper = {
            ")": "(",
            "}": "{",
            "]": "[",
        }

        stack = []

        for br in s:
            if not (br_open := mapper.get(br)):
                stack.append(br)

                continue

            if not stack or stack.pop() != br_open:
                return False

        return not stack
