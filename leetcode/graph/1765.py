class Solution:
    def highestPeak(self, isWater: List[List[int]]) -> List[List[int]]:
        q = deque()
        m, n = len(isWater), len(isWater[0])
        for x in range(m):
            for y in range(n):
                if isWater[x][y] == 1:
                    isWater[x][y] = 0
                    q.append((x, y, 0))
                elif isWater[x][y] == 0:
                    isWater[x][y] = -1

        while q:
            dirs = [1, 0, -1, 0, 1]
            x, y, z = q.popleft()
            for i in range(4):
                nx, ny, nz = x + dirs[i], y + dirs[i + 1], z + 1
                if nx < 0 or nx >= m or ny < 0 or ny >= n:
                    continue
                if isWater[nx][ny] == -1:
                    isWater[nx][ny] = nz
                    q.append((nx, ny, nz))

        return isWater
