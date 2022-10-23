# https://leetcode.com/problems/palindrome-number/
class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x == 0:
            return True

        if x < 0 or x % 10 == 0:
            return False

        rev = 0

        while rev < x:
            x, rem = divmod(x, 10)
            rev = rev * 10 + rem

        return rev == x or rev // 10 == x
