class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        m = len(triangle)
        dp = [float('inf')] * m
        dp[0] = triangle[0][0]
        for i in range(1, m):
            new_dp = [float('inf')] * m
            for j in range(i + 1):
                new_dp[j] = min(dp[j], dp[j - 1] if j - 1 >= 0 else float('inf')) + triangle[i][j]
            dp = new_dp

        # print(dp)
        return min(dp)