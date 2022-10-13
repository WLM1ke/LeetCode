# https://leetcode.com/problems/remove-invalid-parentheses/
from typing import List


class Solution:
    def removeInvalidParentheses(self, s: str) -> List[str]:
        level = {s}

        while True:
            if rez := [substr for substr in level if is_valid(substr)]:
                return rez

            level = {
                substr[:i] + substr[i + 1:]
                for substr in level
                for i in range(len(substr))
            }


def is_valid(s: str) -> bool:
    count = 0

    for symbole in s:
        if symbole == "(":
            count += 1
        elif symbole == ")":
            count -= 1

        if count < 0:
            return False

    return count == 0
