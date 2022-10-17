# https://leetcode.com/problems/most-common-word/
import collections

from typing import List


class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        banned = set(banned)
        banned.add("")

        punct = set(" !?',;.")

        paragraph = "".join(
            " " if let in punct else let.lower()
            for let in paragraph
        )

        par = collections.Counter(
            word
            for word in paragraph.split()
            if word not in banned
        )

        return par.most_common(1)[0][0]
