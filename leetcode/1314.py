class Solution:
    def matrixBlockSum(self, mat: List[List[int]], k: int) -> List[List[int]]:

        m, n = len(mat), len(mat[0])

        def get_prefix(arr):
            cur = sum(arr[: k + 1])
            n = len(arr)
            res = [cur]
            for i in range(1, n):
                left, right = i - k - 1, i + k
                if left >= 0:
                    cur -= arr[left]
                if right < n:
                    cur += arr[right]
                res.append(cur)

            return res

        temp = []
        for row in mat:
            temp.append(get_prefix(row))

        res = [[0] * n for _ in range(m)]
        for i in range(n):
            p = [temp[j][i] for j in range(m)]
            p = get_prefix(p)
            for j in range(m):
                res[j][i] = p[j]

        return res
