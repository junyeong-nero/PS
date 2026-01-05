class Solution:
    def maxMatrixSum(self, matrix: List[List[int]]) -> int:
        n = len(matrix)

        arr = []
        for i in range(n):
            for j in range(n):
                cur = matrix[i][j]
                arr.append(cur)

        count_neg = sum([1 for elem in arr if elem < 0])
        res = sum([abs(elem) for elem in arr])
        if count_neg % 2 == 0:
            return res

        temp = abs(min(arr, key=abs))
        res -= temp * 2
        return res
