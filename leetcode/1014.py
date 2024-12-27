class Solution:
    def maxScoreSightseeingPair(self, values: List[int]) -> int:
        n = len(values)
        res = 0
        values = sorted([(values[i], i) for i in range(n)], reverse=True)
        print(values)
        # i - j < n
        for i in range(n - 1):
            temp = -n
            a = values[i]
            for j in range(i + 1, n):
                b = values[j]
                val = a[0] + b[0] - abs(a[1] - b[1])
                if val >= temp:
                    temp = val
                else:
                    break
            res = max(res, temp)

        return res