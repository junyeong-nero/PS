class Solution:
    def countGoodArrays(self, n: int, m: int, k: int) -> int:
        MOD = 10 ** 9 + 7

        def dfs(cur, size, left):
            if left < 0 or size > n:
                return 0
            if size == n and left == 0:
                return 1
                
            res = 0
            for num in range(1, m + 1):
                diff = 1 if num == cur else 0
                res += dfs(num, size + 1, left - diff)

            return res % MOD
        
        return dfs(0, 0, k)
