# https://leetcode.com/problems/count-and-say/

class Solution:
    def countAndSay(self, n: int) -> str:
        if n == 1:
            return "1"

        base = "1"

        for _ in range(2, n + 1):
            base = _say(base)

        return base


def _say(s):
    prev = s[0]
    count = 1
    rez = []

    for let in s[1:]:
        if let == prev:
            count += 1
        else:
            rez.append(f"{count}{prev}")
            prev = let
            count = 1

    rez.append(f"{count}{prev}")

    return "".join(rez)
