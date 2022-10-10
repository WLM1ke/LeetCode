SYMBOLS = {
    "I": 1,
    "V": 5,
    "X": 10,
    "L": 50,
    "C": 100,
    "D": 500,
    "M": 1000,
}


class Solution:
    def romanToInt(self, s: str) -> int:
        prev = 1
        num = 0

        for symbol in reversed(s):
            val = SYMBOLS[symbol]
            if val < prev:
                num -= val
            else:
                num += val
                prev = val

        return num
