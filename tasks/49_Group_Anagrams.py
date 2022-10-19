# https://leetcode.com/problems/group-anagrams/
from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = {}

        for word in strs:
            groups.setdefault(tuple(sorted(word)), []).append(word)

        return list(groups.values())
