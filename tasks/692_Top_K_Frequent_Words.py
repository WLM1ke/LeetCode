import collections
from typing import List


class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        rez = list(collections.Counter(words).items())
        rez.sort(key=lambda x: (-x[1], x[0]))

        return [rez[i][0] for i in range(k)]
