# https://leetcode.com/problems/valid-palindrome/

class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = "".join(let.lower() for let in s if let.isalnum())

        return s == s[::-1]
