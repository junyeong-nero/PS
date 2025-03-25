class Solution:
    def countPaths(self, n: int, roads: List[List[int]]) -> int:
        MOD = 10 ** 9 + 7

        d = defaultdict(dict)
        for u, v, time in roads:
            d[u][v] = time
            d[v][u] = time
        # print(d)

        dp = [[(float('inf'), 0)] * n for _ in range(n)]
        for i in range(n):
            dp[i][i] = (0, 1)

        for u, v, time in roads:    
            dp[u][v] = (time, 1)
            dp[v][u] = (time, 1)

        def dfs(i, j):
            if dp[i][j] != (float('inf'), 0):
                return dp[i][j]

            min_time, min_count = float('inf'), 0
            for k in range(n):
                a_time, a_count = dfs(i, k)
                b_time, b_count = dfs(k, j)
                time = a_time + b_time
                count = a_count * b_count
                if time < min_time:
                    min_time = time
                    min_count = count

            dp[i][j] = (min_time, min_count)
            return dp[i][j]
        
        return dfs(0, n - 1)

            
            