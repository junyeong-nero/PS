class Solution:
    def putMarbles(self, weights: List[int], k: int) -> int:
        
        n = len(weights)
        dp = dict()

        @cache
        def func(cur, count):
            if (cur, count) in dp:
                return d[(cur, count)]
            if count == 1:
                temp = weights[cur] + weights[-1]
                return temp, temp

            a, b = -float('inf'), float('inf')
            for i in range(cur, n - 1):
                value = weights[i] + weights[cur]
                c, d = func(i + 1, count - 1)
                a, b  = max(a, value + c), min(b, value + d)
            
            dp[(cur, count)] = (a, b)
            return a, b

        res = func(0, k)
        return res[0] - res[1]
