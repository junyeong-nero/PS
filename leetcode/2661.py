class Solution:
    def firstCompleteIndex(self, arr: List[int], mat: List[List[int]]) -> int:
        m, n = len(mat), len(mat[0])
        row, col = [0] * m, [0] * n

        pos = [0] * (m * n)
        for i in range(m):
            for j in range(n):
                pos[mat[i][j] - 1] = (i, j)

        for i in range(len(arr)):
            x, y = pos[arr[i] - 1]
            row[x] += 1
            col[y] += 1
            if row[x] == n or col[y] == m:
                return i

        return 0
