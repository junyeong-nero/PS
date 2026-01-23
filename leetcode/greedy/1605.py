class Solution:
    def restoreMatrix(self, rowSum: List[int], colSum: List[int]) -> List[List[int]]:
        # we will iterate through rows and columns,
        # adding an element with the minimum of the current 
        # required value for each row and column
        # this will take O(n+m) time
        # (ignoring creating the matrix itself of 0s which is O(n*m))
        n, m = len(rowSum), len(colSum)
        mat = [[0] * m for _ in range(n)]
        i, j = 0, 0
        while i < n and j < m:
            if j == m - 1 or rowSum[i] < colSum[j]:
                mat[i][j] = rowSum[i]
                colSum[j] -= rowSum[i]
                i += 1
            else:
                mat[i][j] = colSum[j]
                rowSum[i] -= colSum[j]
                j += 1
        return mat


class Solution:
    def restoreMatrix(self, rowSum: List[int], colSum: List[int]) -> List[List[int]]:
        m, n = len(rowSum), len(colSum)

        res = [[0] * n for _ in range(m)]
        res[0] = colSum

        for i in range(m):
            prefix = 0
            for j in range(n):
                prefix += res[i][j]
                if prefix == float("inf"):
                    # line down
                    res[i + 1][j] = res[i][j]
                    res[i][j] = 0

                elif prefix > rowSum[i]:
                    diff = prefix - rowSum[i]
                    res[i][j] -= diff
                    res[i + 1][j] += diff
                    prefix = float("inf")

        return res

