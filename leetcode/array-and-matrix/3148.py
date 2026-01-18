class Solution:
    def maxScore(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        max_grid = [[float("-inf")] * (n + 1) for _ in range(m + 1)]

        res = float("-inf")
        # score[i, j] = max(grid[i + 1:][j + 1:]) - grid[i][j]

        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                max_grid[i][j] = max(max_grid[i][j + 1], max_grid[i + 1][j], grid[i][j])
                score = max(
                    max_grid[i][j + 1] - grid[i][j],
                    max_grid[i + 1][j] - grid[i][j],
                )
                res = max(res, score)

        # print(max_grid)
        return res
