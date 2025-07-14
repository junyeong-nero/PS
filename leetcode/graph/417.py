class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:

        m, n = len(heights), len(heights[0])
        po = [[False] * n for _ in range(m)]
        ao = [[False] * n for _ in range(m)]

        po_start = []
        ao_start = []
        for i in range(m):
            po_start.append((i, 0))
            ao_start.append((i, n - 1))
            po[i][0] = True
            ao[i][-1] = True

        for j in range(n):
            po_start.append((0, j))
            ao_start.append((m - 1, j))
            po[0][j] = True
            ao[m - 1][j] = True

        def func(start_points, target):
            q = deque(start_points)
            while q:
                x, y = q.popleft()

                dirs = [1, 0, -1, 0, 1]
                for i in range(4):
                    nx, ny = x + dirs[i], y + dirs[i + 1]
                    if nx < 0 or nx >= m or ny < 0 or ny >= n:
                        continue
                    if target[nx][ny]:
                        continue
                    if heights[nx][ny] < heights[x][y]:
                        continue

                    target[nx][ny] = True
                    q.append((nx, ny))

        func(po_start, po)
        func(ao_start, ao)

        # print(po)
        # print(ao)

        res = []
        for x in range(m):
            for y in range(n):
                if ao[x][y] and po[x][y]:
                    res.append([x, y])

        return res
