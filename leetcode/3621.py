class Solution:
    def popcountDepth(self, n: int, k: int) -> int:

        def popcount(num):
            return bin(num).count("1")

        dp = dict()
        dp[1] = 0

        def popcount_depth(x):
            if x in dp:
                return dp[x]

            c = popcount(x)
            dp[x] = popcount_depth(c) + 1
            return dp[x]

        res = 0
        for i in range(1, n + 1):
            depth = popcount_depth(i)
            if depth == k:
                res += 1

        return res
