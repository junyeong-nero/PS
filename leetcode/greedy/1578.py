class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        colors = list(colors)
        n = len(colors)

        i = cost = 0
        while i < n:
            j = i
            _sum, _max = 0, 0
            while j < n and colors[i] == colors[j]:
                _sum += neededTime[j]
                _max = max(_max, neededTime[j])
                j += 1
            cost += _sum - _max
            i = j

        return cost


class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        colors = list(colors)
        n = len(colors)

        i = cost = 0
        while i < n:
            j = i
            _sum, _max = 0, 0
            while j < n and colors[i] == colors[j]:
                _sum += neededTime[j]
                _max = max(_max, neededTime[j])
                j += 1
            cost += _sum - _max
            i = j

        return cost
