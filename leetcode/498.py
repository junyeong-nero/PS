class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        m, n = len(mat), len(mat[0])
        res = []
        for level in range(m + n - 1):
            if level % 2 == 0:
                temp = range(level, -1, -1)
            else:
                temp = range(level + 1)

            # print(level)
            for x in temp:
                y = level - x
                if 0 <= x < m and 0 <= y < n:
                    # print(x, y)
                    res.append(mat[x][y])

        return res
