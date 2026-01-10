class Solution:
    def maxDistance(self, arrays: List[List[int]]) -> int:

        min_arr = sorted([arr[0] for arr in arrays])
        max_arr = sorted([arr[-1] for arr in arrays])

        n = len(arrays)
        res = float("-inf")

        for i in range(n):
            m, M = arrays[i][0], arrays[i][-1]
            if m == min_arr[0] and M == max_arr[-1]:
                res = max(res, max_arr[-2] - min_arr[0])
                res = max(res, max_arr[-1] - min_arr[1])

        if res == float("-inf"):
            res = max_arr[-1] - min_arr[0]

        return res
