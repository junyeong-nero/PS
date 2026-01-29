class Solution:
    def coloredCells(self, n: int) -> int:
        # p(n) = 4 * n - 4
        # 1 + p(1) + p(2) ... p(n)  = 1 + 4 * (n + 1) * n / 2 - 4 * n
        return 1 + 4 * (n + 1) * n // 2 - 4 * n
