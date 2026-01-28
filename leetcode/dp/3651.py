class Solution:
    def minCost(self, grid: list[list[int]], k: int) -> int:
        m, n = len(grid), len(grid[0])
        size = m * n

        # 1. 모든 셀의 (값, 행, 열) 정보를 담은 리스트 생성 후 내림차순 정렬
        # 이는 순간이동 시 '값이 같은 셀들'을 효율적으로 처리하기 위함으로 보입니다.
        idx = [(grid[i][j], i, j) for i in range(m) for j in range(n)]
        idx.sort(reverse=True)

        # 2. 초기 DP 테이블 설정 (0,0에서 시작하는 최소 비용)
        dp = [[float("inf")] * n for _ in range(m)]

        # 시작점 초기화 (grid[0][0] 비용을 더하며 시작하려면 수정 필요할 수 있음)
        dp[0][0] = 0

        # 3. 기본적인 상->하, 좌->우 이동에 따른 최소 비용 계산 (순간이동 0회차)
        for i in range(m):
            for j in range(n):
                if i:
                    dp[i][j] = min(dp[i][j], dp[i - 1][j] + grid[i][j])
                if j:
                    dp[i][j] = min(dp[i][j], dp[i][j - 1] + grid[i][j])

        # 4. k번의 순간이동 기회 처리
        for _ in range(k):
            # tele: 순간이동 후 각 셀에 도달하는 최소 비용을 저장
            tele = [[float("inf")] * n for _ in range(m)]
            tmin = float("inf")  # 현재까지 탐색한 셀 중 최소 DP 값
            p = 0

            # 5. 값을 기준으로 그룹화하여 순간이동 비용 갱신
            # (값이 큰 셀에서 작은 셀로 가거나, 같은 그룹 내에서의 전이를 처리하는 로직)

            # grid 값이 큰 놈부터 tmin을 최소화
            # 나중엔 작은 놈이 오면 -> 큰놈으로 텔레포트 할 수 있으나, tmin 값으로 업데이트 하면 됨.
            while p < size:
                q, v = p, idx[p][0]
                # 같은 값을 가진 셀들을 한 번에 처리
                while q < size and idx[q][0] == v:
                    x, i, j = idx[q]
                    tmin = min(tmin, dp[i][j])  # 현재 그룹까지의 최소 비용 갱신
                    q += 1

                # 동일 값 그룹 내 모든 셀에 현재까지의 최소 비용(tmin) 할당
                for r in range(p, q):
                    _, i, j = idx[r]
                    tele[i][j] = tmin
                p = q

            # 6. 순간이동 이후 다시 기본적인 이동(상하좌우)을 고려하여 DP 업데이트
            ndp = [row[:] for row in tele]
            for i in range(m):
                for j in range(n):
                    if i:
                        ndp[i][j] = min(ndp[i][j], ndp[i - 1][j] + grid[i][j])
                    if j:
                        ndp[i][j] = min(ndp[i][j], ndp[i][j - 1] + grid[i][j])
            dp = ndp  # 다음 k회차를 위해 dp 테이블 갱신

        # 7. 최종 목적지(우측 하단)의 최소 비용 반환
        return dp[m - 1][n - 1]


# class Solution:
#     def minCost(self, grid: List[List[int]], k: int) -> int:
#         m, n = len(grid), len(grid[0])

#         # cur : i, j
#         # teleport to grid[x][y] < grid[i][j], at most k times
#         # move to right / down with cost grid[x][y]

#         maps = defaultdict(list)

#         for i in range(m):
#             for j in range(n):
#                 maps[grid[i][j]].append((i, j))

#         @cache
#         def dfs(x, y, left=k):

#             if x == m - 1 and y == n - 1:
#                 return 0

#             res = float("inf")
#             cur = grid[x][y]

#             # TP
#             if left > 0:
#                 for key, value in maps.items():
#                     if key > cur:
#                         continue
#                     for i, j in value:
#                         if i <= x and j <= y:
#                             continue
#                         res = min(res, dfs(i, j, left - 1))

#             # move
#             if x + 1 < m:
#                 res = min(res, grid[x + 1][y] + dfs(x + 1, y, left))
#             if y + 1 < n:
#                 res = min(res, grid[x][y + 1] + dfs(x, y + 1, left))

#             return res

#         res = dfs(0, 0)
#         return res
