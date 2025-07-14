class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:

        m, n = len(matrix), len(matrix[0])

        res = [matrix[0][0]]
        matrix[0][0] = None

        dirs_index = 0
        dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]

        x, y = 0, 0

        count = 1
        while count < m * n:
            dx, dy = dirs[dirs_index]
            # print(dx, dy)

            while (
                0 <= x + dx < m
                and 0 <= y + dy < n
                and matrix[x + dx][y + dy] is not None
            ):
                res.append(matrix[x + dx][y + dy])
                count += 1
                matrix[x + dx][y + dy] = None
                x, y = x + dx, y + dy

            # print(res)
            dirs_index = (dirs_index + 1) % 4

        return res
