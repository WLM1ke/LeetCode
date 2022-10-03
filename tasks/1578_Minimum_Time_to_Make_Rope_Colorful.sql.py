# https://leetcode.com/problems/minimum-time-to-make-rope-colorful/
class Solution:
    def minCost(self, colors: str, neededTime: list[int]) -> int:
        time_total = 0
        color_pre = ""
        time_max = 0

        for color, time_remove in zip(colors, neededTime):
            if color != color_pre:
                color_pre = color
                time_max = time_remove

                continue

            time_total += min(time_max, time_remove)
            time_max = max(time_max, time_remove)

        return time_total
