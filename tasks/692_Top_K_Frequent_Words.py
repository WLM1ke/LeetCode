import collections
import heapq
from typing import List


class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        counts = collections.Counter(words)

        return heapq.nsmallest(k, counts, key=lambda x: (-counts[x], x))
