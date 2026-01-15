class Solution:
    def sellingWood(self, m: int, n: int, prices: List[List[int]]) -> int:

        # divide and conqur?
        # m, n boards divide in vertically or horizontally
        # p + q, n / m, r + s
        # if one shapes in (m, n), then sell it
        #      or keep branch this.
        # any of shapes in (m, n), return 0
        # p, q in boundary

        # DP style solutions?
        # dp[i][j] = maximum cost with i, j size boards
        # dp[i][j] = (dp[i - x][j] + dp[x][j]) for x in range(i // 2),
        #            (dp[i][j - y] + dp[i][j]) for y in range(j // 2)

        dp = [[0] * (n + 1) for _ in range(m + 1)]
        for x, y, cost in prices:
            dp[x][y] = cost

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                h = max([0] + [dp[i - x][j] + dp[x][j] for x in range(1, i // 2 + 1)])
                v = max([0] + [dp[i][j - y] + dp[i][y] for y in range(1, j // 2 + 1)])
                dp[i][j] = max(dp[i][j], h, v)

        # print(dp)
        return dp[-1][-1]
