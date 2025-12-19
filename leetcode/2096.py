class Solution:
    def constructProductMatrix(self, grid: List[List[int]]) -> List[List[int]]:
        m, n = len(grid), len(grid[0])
        MOD = 12345

        columns = []
        counter = Counter()
        x0, y0 = -1, -1
        value = 1

        for x in range(m):
            for y in range(n):
                cur = grid[x][y] % MOD
                counter[cur] += 1
                if cur == 0:
                    x0, y0 = x, y
                else:
                    value *= grid[x][y]
                    # value = value % MOD

        if counter[0] >= 2:
            # return all zero grids
            return [[0] * n for _ in range(m)]

        if counter[0] >= 1:
            # return all zero grids excepts x0, y0
            grid = [[0] * n for _ in range(m)]
            grid[x0][y0] = value % MOD
            return grid

        for x in range(m):
            for y in range(n):
                grid[x][y] = value // grid[x][y]
                grid[x][y] = grid[x][y] % MOD

        return grid