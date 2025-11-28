class Solution:
    def kConcatenationMaxSum(self, arr: List[int], k: int) -> int:
        res = 0
        n = len(arr)
        MOD = 10**9 + 7

        if all([elem < 0 for elem in arr]):
            return res

        max_value = max(arr)
        sum_value = sum(arr)
        res = max(res, max_value, sum_value * k)

        prefix_L = [0]
        prefix_R = [0]

        for i in range(n):
            prefix_L.append(prefix_L[-1] + arr[i])
            prefix_R.append(prefix_R[-1] + arr[n - 1 - i])

        prefix_R = prefix_R[::-1]
        # prefix_L[i] : sum(arr[:i])
        # prefix_R[i] : sum(arr[j:])

        u, v = max(prefix_L), max(prefix_R)
        print(u, v)

        res = max(res, u, v)

        min_value = float("inf")
        for value in prefix_L:
            min_value = min(min_value, value)
            res = max(res, value - min_value)

        if k >= 2:
            res = max(res, u + v)
            res = max(res, u + v + sum_value * (k - 2))

        if res > MOD:
            res = res % MOD

        return res
