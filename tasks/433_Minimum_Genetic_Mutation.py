# https://leetcode.com/problems/minimum-genetic-mutation/
import collections

_GENE_SIZE = 8
_LET = "ACGT"


class Solution(object):
    def minMutation(self, start, end, bank):
        """
        :type start: str
        :type end: str
        :type bank: List[str]
        :rtype: int
        """
        bank = set(bank)
        que = collections.deque([(start, 0)])

        while que:
            gen, count = que.popleft()
            if gen == end:
                return count

            for pos in range(_GENE_SIZE):
                for lt in _LET:
                    if lt == gen[pos]:
                        continue

                    child = gen[:pos] + lt + gen[pos + 1:]
                    if child not in bank:
                        continue

                    bank.remove(child)
                    que.append((child, count + 1))

        return -1
