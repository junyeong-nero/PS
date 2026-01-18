class Solution:
    def rearrangeSticks(self, n: int, k: int) -> int:

        MOD = 10**9 + 7
        # dp[i][j] = with i sticks, j visible sticks
        dp = [[0] * (k + 1) for _ in range(n + 1)]

        for i in range(min(n, k) + 1):
            dp[i][i] = 1

        for i in range(1, n + 1):
            for j in range(1, k + 1):
                dp[i][j] = dp[i - 1][j - 1] + dp[i - 1][j] * (i - 1)
                dp[i][j] = dp[i][j] % MOD
                # dp[i - 1][j - 1] : tallest sticks at last
                # dp[i - 1][j] * (i - 1) : smallest sticks behind any sticks

        # print(dp)
        return dp[-1][-1]
