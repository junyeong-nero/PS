class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        res = 0
        for col in grid:
            res += bisect_left(col[::-1], 0)
        return res