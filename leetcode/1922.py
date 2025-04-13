class Solution:
    def countGoodNumbers(self, n: int) -> int:
        MOD = 10 ** 9 + 7

        # 5 (0, 2, 4, 6, 8)
        # 4 (2, 3, 5, 7)
        odd = n // 2
        even = n - odd 

        return (5 ** even) * (4 ** odd) % MOD