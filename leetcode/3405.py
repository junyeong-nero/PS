class Solution:
    def countGoodArrays(self, n: int, m: int, k: int) -> int:
        # k = 5
        # [a, a]  5
        # [a, a, a]

        MOD = 10 ** 9 + 7

        if k == 0:
            return m ** n % MOD

        dp = [[0] * (k + 1) for _ in range(k + 1)]
        dp[1][1] = 1
        for i in range(1, k + 1):
            for j in range(1, i):
                dp[i][j] = dp[i - 1][j - 1] + dp[i - j][j]
        print(dp)

        def P(a, b):
            if b == 1 or a == b:
                return 1
            # 1이 있는 경우 -> 1만 추가하면 되니: P(a - 1, b - 1)
            # 1이 없는 경우 -> 적어도 b개의 항목이 2가 되어야 함: P(a - b, b)
            return P(a - 1, b - 1) + P(a - b, b)

        def P_all(a):
            arr = [P(a, i) for i in range(1, a + 1)]
        
        return 0
                