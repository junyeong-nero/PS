class Solution:
    def maxProfit(self, prices: List[int], strategy: List[int], k: int) -> int:

        n = len(prices)

        res = sum([prices[i] * strategy[i] for i in range(n)])
        new_strategy = strategy[:]
        for i in range(k):
            if i < k // 2:
                new_strategy[i] = 0
            else:
                new_strategy[i] = 1

        start, end = 0, k
        value = sum([prices[i] * new_strategy[i] for i in range(n)])
        res = max(res, value)

        for i in range(n - k):
            mid = (start + end) // 2
            value += (strategy[start] - 0) * prices[start]
            value += (0 - 1) * prices[mid]
            value += (1 - strategy[end]) * prices[end]
            res = max(res, value)

            # start : 0 -> original
            # mid : 1 -> 0
            # end : orignal -> 1

            start += 1
            end += 1

        return res
