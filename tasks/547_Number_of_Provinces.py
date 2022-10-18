# https://leetcode.com/problems/number-of-provinces/
from typing import List


class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        visited = set()
        provinces = 0

        stack = []

        for city in range(len(isConnected)):
            if len(visited) == len(isConnected):
                break

            if city in visited:
                continue

            visited.add(city)
            stack.append(city)
            provinces += 1

            while stack and len(visited) < len(isConnected):
                for near, flag in enumerate(isConnected[stack.pop()]):
                    if flag and near not in visited:
                        visited.add(near)
                        stack.append(near)

        return provinces
