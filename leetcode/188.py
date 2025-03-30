class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        
        n = len(prices)

        benefit = []
        for i in range(1, n):
            for j in range(i):
                value = prices[i] - prices[j]
                if value > 0:
                    benefit.append((j, i, value))
        # print(benefit)

        d = dict()

        @cache
        def func(cur, cost, count):
            if (cur, cost, count) in d:
                return d[(cur, cost, count)]
            if count == 0:
                return cost
            res = cost
            for start, end, value in benefit:
                if start <= cur:
                    continue
                res = max(res, func(end, cost + value, count - 1))
            d[(cur, cost, count)] = res
            return res

        return func(-1, 0, k)