# https://leetcode.com/problems/find-positive-integer-solution-for-a-given-equation/
from typing import List


# This is the custom function interface.
# You should not implement it, or speculate about its implementation
class CustomFunction:
    # Returns f(x, y) for any given positive integers x and y.
    # Note that f(x, y) is increasing with respect to both x and y.
    # i.e. f(x, y) < f(x + 1, y), f(x, y) < f(x, y + 1)
    def f(self, x, y):
        pass


class Solution:
    def findSolution(self, customfunction: 'CustomFunction', z: int) -> List[List[int]]:

        rez = []

        for x in range(1, 1001):
            if point := _find(customfunction, x, z):
                rez.append(point)

        return rez


def _find(customfunction, x, z):
    low = 0
    high = 1000

    while low + 1 < high:
        mid = (low + high) >> 1

        if customfunction.f(x, mid) < z:
            low = mid
        else:
            high = mid

    if customfunction.f(x, high) == z:
        return [x, high]

    return None
