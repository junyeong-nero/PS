class Solution:
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        n = len(envelopes)
        envelopes = sorted(envelopes)
        print(envelopes)

        @cache
        def dfs(cur, value):
            w, h = envelopes[cur] if cur >= 0 else [0, 0]
            start = bisect_left(envelopes, w + 1, key=lambda x: x[0])
            start = max(cur + 1, start)

            res = value
            for i in range(start, n):
                if envelopes[i][0] > w and envelopes[i][1] > h:
                    res = max(res, dfs(i, value + 1))

            return res

        res = dfs(-1, 0)
        return res
