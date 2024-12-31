from typing import List
from functools import cache

class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        
        @cache
        def dfs(index, cover):
            if index >= len(days):
                return 0
            day = days[index]
            if day <= cover:
                return dfs(index + 1, cover)

            temp = float('inf')
            temp = min(temp, dfs(index + 1, day) + costs[0])
            temp = min(temp, dfs(index + 1, day + 6) + costs[1])
            temp = min(temp, dfs(index + 1, day + 29) + costs[2])
            return temp

        return dfs(0, 0)