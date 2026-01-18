class Solution:
    def largestMagicSquare(self, grid: List[List[int]]) -> int:

        m, n = len(grid), len(grid[0])

        vertical = []
        for i in range(m):
            column = grid[i]
            prefix = [0]
            for num in column:
                prefix.append(prefix[-1] + num)
            vertical.append(prefix)

        horizontal = []
        for j in range(n):
            row = [grid[i][j] for i in range(m)]
            prefix = [0]
            for num in row:
                prefix.append(prefix[-1] + num)
            horizontal.append(prefix)

        def check(i, j, k):
            # check with [i, j] ~ [i + k, j + k] is magic square
            # 1. vertical sum     -> prefix sum
            # 2. check horizontal -> prefix sum
            # 3. check diagonal sum
            target = -1

            v = [vertical[x][j + k + 1] - vertical[x][j] for x in range(i, i + k + 1)]
            h = [
                horizontal[y][i + k + 1] - horizontal[y][i] for y in range(j, j + k + 1)
            ]

            diagonal = [
                sum([grid[i + x][j + x] for x in range(k + 1)]),
                sum([grid[i + x][j + k - x] for x in range(k + 1)]),
            ]

            # print(i, j, k)
            # print(v, h)
            # print(diagonal)

            temp = set(v + h + diagonal)
            return len(temp) == 1

        res = 1
        for i in range(m):
            for j in range(n):
                k = min(m - i, n - j) - 1
                while k > 0:
                    if check(i, j, k):
                        res = max(res, k + 1)
                        break
                    
                    k -= 1

        return res
