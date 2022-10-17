# https://leetcode.com/problems/add-binary/

class Solution:
    def addBinary(self, a: str, b: str) -> str:
        ab = int(a, 2)
        bb = int(b, 2)

        return str(bin(ab + bb))[2:]
