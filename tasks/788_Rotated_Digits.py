# https://leetcode.com/problems/rotated-digits/
class Solution:
    def rotatedDigits(self, n: int) -> int:
        bad = {"3", "4", "7"}
        good = {"2", "5", "6", "9"}

        count = 0

        for num in range(1, n + 1):
            cur = set(str(num))

            if (not (cur & bad)) and (cur & good):
                count += 1

        return count
