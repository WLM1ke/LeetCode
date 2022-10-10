# https://leetcode.com/problems/valid-parentheses/

class Solution:
    def isValid(self, s: str) -> bool:
        mapper = {
            ")": "(",
            "]": "[",
            "}": "{",
        }

        stack = []

        for br in s:
            if br not in mapper:
                stack.append(br)

                continue

            if not stack or stack[-1] != mapper[br]:
                return False

            stack.pop()

        return not stack
