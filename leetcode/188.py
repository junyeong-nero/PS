class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        n = len(prices)
        if not prices or k == 0:
            return 0

        # If k is large enough, use unlimited transactions strategy
        if k >= n // 2:
            return sum(max(prices[i + 1] - prices[i], 0) for i in range(n - 1))

        # DP table
        dp = [[0] * n for _ in range(k + 1)]

        for i in range(1, k + 1):
            maxDiff = -prices[0]  # Maximum of (dp[i-1][m] - prices[m])
            for j in range(1, n):
                dp[i][j] = max(dp[i][j - 1], prices[j] + maxDiff)
                maxDiff = max(maxDiff, dp[i - 1][j] - prices[j])

        return dp[k][n - 1]
