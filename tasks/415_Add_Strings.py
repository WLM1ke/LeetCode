# https://leetcode.com/problems/add-strings/

class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        over = 0
        rez = []
        pointer = 0

        while over or max(len(num1), len(num2)) > pointer:
            if pointer < len(num1):
                over += ord(num1[~pointer]) - ord("0")

            if pointer < len(num2):
                over += ord(num2[~pointer]) - ord("0")

            over, val = divmod(over, 10)
            rez.append(str(val))
            pointer += 1

        return "".join(reversed(rez))
