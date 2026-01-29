class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        n = len(arr)

        diff = []
        for i in range(n - 1):
            diff.append(arr[i + 1] - arr[i])

        # print(diff)
        m = len(diff)
        i = 0
        res = 1
        while i < m:
            if diff[i] == 0:
                i += 1
                continue

            pos = 1 if diff[i] < 0 else -1
            j = i + 1
            while j < m and pos * diff[j] > 0:
                j += 1
                pos *= -1
            # print(i, j)
            res = max(res, j - i + 1)
            i = j

        return res
