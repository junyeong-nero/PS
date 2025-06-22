class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        m = len(triangle)
        
        dp = [[float('inf')] * m for _ in range(m)]
        dp[0][0] = triangle[0][0]
        for i in range(1, m):
            for j in range(i + 1):
                dp[i][j] = min(dp[i - 1][j], dp[i - 1][j - 1] if j - 1 >= 0 else float('inf')) + triangle[i][j]

        # print(dp)
        return min(dp[-1])