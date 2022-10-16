# https://leetcode.com/problems/beautiful-arrangement/

class Solution:
    def countArrangement(self, n: int) -> int:
        return permutations(list(range(1, n + 1)))


def permutations(seq, start=0, counter=0):
    size = len(seq)

    if start == size - 1:
        return counter + (size % seq[start] == 0)

    for i in range(start, size):
        if (seq[i] % (start + 1) == 0) or ((start + 1) % seq[i] == 0):
            seq[start], seq[i] = seq[i], seq[start]
            counter = permutations(seq, start + 1, counter)
            seq[start], seq[i] = seq[i], seq[start]

    return counter
