# https://leetcode.com/problems/remove-all-adjacent-duplicates-in-string/

class Solution:
    def removeDuplicates(self, s: str) -> str:
        rez = []
        for lt in s:
            if rez and rez[-1] == lt:
                rez.pop()
            else:
                rez.append(lt)

        return "".join(rez)
