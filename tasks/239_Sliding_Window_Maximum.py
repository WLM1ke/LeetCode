# https://leetcode.com/problems/sliding-window-maximum/
import collections

from typing import List


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        que = collections.deque()

        maxs = []

        for pos, num in enumerate(nums):
            while que and que[-1][1] < num:
                que.pop()

            que.append((pos, num))

            if que[0][0] + k == pos:
                que.popleft()

            if pos >= k - 1:
                maxs.append(que[0][1])

        return maxs
