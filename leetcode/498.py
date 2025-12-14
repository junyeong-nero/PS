class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        m, n = len(mat), len(mat[0])
        res = []
        d = defaultdict(list)
        for x in range(m):
            for y in range(n):
                d[x + y].append(mat[x][y])

        for level in d:
            res += d[level][::-1] if level % 2 == 0 else d[level]

        return res
