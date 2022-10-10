# https://leetcode.com/problems/partitioning-into-minimum-number-of-deci-binary-numbers/

class Solution:
    def minPartitions(self, n: str) -> int:
        return int(max(n))


class Solution2:
    def minPartitions(self, n: str) -> int:
        rez = ""
        for i in n:
            rez = max(i, rez)

            if rez == "9":
                return 9

        return int(rez)
