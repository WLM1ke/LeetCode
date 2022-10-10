# https://leetcode.com/problems/guess-number-higher-or-lower/

# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
def guess(num: int) -> int:
    pass


class Solution:
    def guessNumber(self, n: int) -> int:
        l, r = 0, n

        while l + 1 < r:
            mid = (l + r) // 2

            match guess(mid):
                case 0:
                    return mid
                case 1:
                    l = mid
                case _:
                    r = mid

        return r
