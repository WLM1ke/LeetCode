# https://leetcode.com/problems/longest-repeating-character-replacement/

import collections


class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        letters = collections.defaultdict(int)
        size = 0

        for pos, letter in enumerate(s):
            letters[letter] += 1

            if size + 1 <= max(letters.values()) + k:
                size += 1
            else:
                letters[s[pos - size]] -= 1

        return size
