# https://leetcode.com/problems/reverse-vowels-of-a-string/
class Solution:
    def reverseVowels(self, s: str) -> str:
        rez = list(s)
        vowels = {"a", "e", "i", "o", "u"}

        start = 0
        end = len(s) - 1

        while start < end:
            if rez[start].lower() not in vowels:
                start += 1
            elif rez[end].lower() not in vowels:
                end -= 1
            else:
                rez[start], rez[end] = rez[end], rez[start]
                start += 1
                end -= 1

        return "".join(rez)
