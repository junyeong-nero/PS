class Solution(object):
    def minDeletionSize(self, strs):

        m, n = len(strs), len(strs[0])
        dp = [1] * n
        # dp[i]: number of columns to keep in strs[i:]
        # dp[n - 1] = 1

        for i in range(n - 2, -1, -1):
            for j in range(i + 1, n):
                if all(row[i] <= row[j] for row in strs):
                    dp[i] = max(dp[i], 1 + dp[j])

        return n - max(dp)
