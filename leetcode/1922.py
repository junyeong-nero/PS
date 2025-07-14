class Solution:
    def countGoodNumbers(self, n: int) -> int:
        MOD = 10**9 + 7

        odd = n // 2
        even = n - odd

        # a = (5 ** even) * (4 ** odd)
        # res = 20 ** odd % MOD

        # use pow function rather than ** operator
        res = pow(20, odd, MOD)
        if odd != even:
            res = (5 * res) % MOD
        return res
