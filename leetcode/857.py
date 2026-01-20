import heapq


class Solution:
    def mincostToHireWorkers(
        self, quality: List[int], wage: List[int], k: int
    ) -> float:
        total_quality = 0
        min_wage = float("inf")

        heap = []
        for q, w in sorted(zip(quality, wage), key=lambda x: x[1] / x[0]):
            heapq.heappush(heap, -q)
            total_quality += q
            if len(heap) > k:
                total_quality += heapq.heappop(heap)

            if len(heap) == k:
                min_wage = min(min_wage, total_quality * w / q)

        return min_wage


class Solution:
    def mincostToHireWorkers(
        self, quality: List[int], wage: List[int], k: int
    ) -> float:
        n = len(quality)
        ratio = [wage[i] / quality[i] for i in range(n)]

        # sorting
        indices = sorted(range(n), key=lambda x: ratio[x])
        min_q = []
        res = float("inf")

        for i in indices:
            cur_q = quality[i]
            j = bisect_left(min_q, cur_q)
            min_q.insert(j, cur_q)
            # print(min_q)

            if len(min_q) >= k:
                res = min(res, sum(min_q[:k]) * ratio[i])

        return res

        # DFS with cache

        # @cache
        # def dfs(cur, size=0, max_ratio=-1, sum_quality=0):
        #     if size == k:
        #         return max_ratio * sum_quality
        #     if cur >= n:
        #         return float("inf")

        #     res = float("inf")
        #     res = min(res, dfs(cur + 1, size, max_ratio, sum_quality))
        #     res = min(
        #         res,
        #         dfs(
        #             cur + 1,
        #             size + 1,
        #             max(max_ratio, ratio[cur]),
        #             sum_quality + quality[cur],
        #         ),
        #     )
        #     return res

        # res = dfs(0)
        # return res

        # DP

        # dp[i][j] = sum of quality, maximum ratio in workers[:i] and j workers
        # dp[i][j] =

        # last = dp[i - 1][j][0] * dp[i - 1][j][1]
        # new = (dp[i - 1][j - 1][0] + wage[i]) * max(dp[i - 1][j - 1][1], ratio[i])
        # dp = [[(0, -1)] * (k + 1) for _ in range(n + 1)]

        # for j in range(1, k + 1):
        #     for i in range(1, n + 1):
        #         last_1 = dp[i - 1][j][0] * dp[i - 1][j][1]
        #         last_2 = dp[i][j - 1][0] * dp[i][j - 1][1]

        #         new_ratio = max(dp[i - 1][j - 1][1], ratio[i - 1])
        #         new_quali = dp[i - 1][j - 1][0] + quality[i - 1]
        #         new = new_quali * new_ratio
        #         temp = min(last_1, last_2, new)

        #         if (i == 1 or j == 1):
        #             dp[i][j] = (new_quali, new_ratio)
        #         elif temp == new:
        #             dp[i][j] = (new_quali, new_ratio)
        #         elif temp == last_1:
        #             dp[i][j] = dp[i - 1][j]
        #         elif temp == last_2:
        #             dp[i][j] = dp[i][j - 1]

        # print(dp)
        # return dp[-1][-1][0] * dp[-1][-1][1]
