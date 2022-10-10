# https://leetcode.com/problems/group-anagrams/
from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = {}

        for anagram in strs:
            gr = groups.setdefault(tuple(sorted(anagram)), [])
            gr.append(anagram)

        return [gr for gr in groups.values()]
