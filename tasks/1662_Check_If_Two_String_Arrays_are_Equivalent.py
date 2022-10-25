# https://leetcode.com/problems/check-if-two-string-arrays-are-equivalent/
from typing import List


class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        try:
            for lt1, lt2 in zip(let_gen(word1), let_gen(word2), strict=True):
                if lt1 != lt2:
                    return False
        except:
            return False

        return True


def let_gen(words):
    for word in words:
        yield from word
