class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        
        n = len(prices)
        prefix = [(prices[0], 0)]
        for i in range(1, n):

            temp = prefix[-1]
            if prices[i] < temp[0]:
                temp = (prices[i], i)

            prefix.append(temp)
    
        benefit = [(prefix[i][1], i, prices[i] - prefix[i][0]) for i in range(n) if prices[i] - prefix[i][0] > 0]
        # print(benefit)

        def func(cur, cost):
            res = cost
            for start, end, value in benefit:
                if start <= cur:
                    continue
                res = max(res, func(end, cost + value))
            return res

        return func(-1, 0)