# https://leetcode.com/problems/add-binary/

class Solution:
    def addBinary(self, a: str, b: str) -> str:
        rez = [""] * (max(len(a), len(b)) + 1)

        pointer = -1
        over = 0

        while over or pointer >= -len(a) or pointer >= -len(b):
            if pointer >= -len(a):
                over += a[pointer] == "1"

            if pointer >= -len(b):
                over += b[pointer] == "1"

            over, num = divmod(over, 2)
            rez[pointer] = str(num)
            pointer -= 1

        return "".join(rez)
