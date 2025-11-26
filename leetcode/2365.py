class Solution:
    def numberOfPaths(self, grid: List[List[int]], k: int) -> int:
        m, n = len(grid), len(grid[0])
        # if k == 1:
        #     return int(factorial(m + n - 2) / factorial(n - 1) / factorial(m - 1))

        dp = [[[0 for _ in range(k)] for _ in range(n)] for _ in range(m)]
        dp[0][0][grid[0][0] % k] = 1
        
        for x in range(m):
            for y in range(n):
                A = dp[x - 1][y] if x > 0 else ([0] * k)
                B = dp[x][y - 1] if y > 0 else ([0] * k)
                mod = grid[x][y] % k
                for i in range(k):
                    temp = dp[x][y][(i + mod) % k] + A[i] + B[i]
                    temp = temp % (10 ** 9 + 7)                    
                    dp[x][y][(i + mod) % k] = temp

        return dp[x][y][0]