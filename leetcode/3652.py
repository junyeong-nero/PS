class Solution:
    def maxProfit(self, prices: List[int], strategy: List[int], k: int) -> int:

        n = len(prices)

        def get_benefit(boundary=[-1, -1]):
            start, end = boundary
            mid = (start + end) // 2

            def get_strategy():
                if i < start or i > end:
                    return strategy[i]
                elif i <= mid:
                    return 0
                else:
                    return 1

            res = 0
            for i in range(n):
                st = get_strategy()
                res += prices[i] * st

            return res

        res = get_benefit()

        for i in range(0, n - k + 1):
            boundary = [i, i + k - 1]
            res = max(res, get_benefit(boundary))

        return res
