# https://leetcode.com/problems/find-common-characters/
import collections
from typing import List


class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        common = collections.Counter(words[0])

        for word in words:
            common &= collections.Counter(word)

        return list(common.elements())
