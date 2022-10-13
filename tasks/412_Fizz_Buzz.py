# https://leetcode.com/problems/fizz-buzz/
from typing import List


class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        rez = []

        for i in range(1, n + 1):
            if i % 15 == 0:
                rez.append("FizzBuzz")
            elif i % 5 == 0:
                rez.append("Buzz")
            elif i % 3 == 0:
                rez.append("Fizz")
            else:
                rez.append(str(i))

        return rez
