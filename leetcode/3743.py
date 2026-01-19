fmax = lambda a, b: b if b > a else a


class Solution:
    # 3573. Best Time to Buy and Sell Stock V
    def maximumProfit(self, prices: List[int], k: int) -> int:
        f = [[-inf] * 3 for _ in range(k + 2)]
        for j in range(1, k + 2):
            f[j][0] = 0
        for p in prices:
            for j in range(k + 1, 0, -1):
                f[j][0] = fmax(f[j][0], fmax(f[j][1] + p, f[j][2] - p))
                f[j][1] = fmax(f[j][1], f[j - 1][0] - p)
                f[j][2] = fmax(f[j][2], f[j - 1][0] + p)
        return f[-1][0]

    def maximumScore(self, nums: List[int], k: int) -> int:
        max_i = nums.index(max(nums))
        ans1 = self.maximumProfit(
            nums[max_i:] + nums[:max_i], k
        )  # nums[max_i] is the first element.
        ans2 = self.maximumProfit(
            nums[max_i + 1 :] + nums[: max_i + 1], k
        )  # nums[max_i] is the last element.
        return fmax(ans1, ans2)


class Solution:
    def maximumScore(self, A: List[int], K: int) -> int:
        N = len(A)

        def solve(A):
            dp = list(accumulate(A, max))
            for i, lo in enumerate(accumulate(A, min)):
                dp[i] -= lo
            ans = dp[N - 1]

            for layer in range(K - 1):
                ndp = [-inf] * N
                X = Y = -inf
                for j in range(1, N):
                    X = max(X, dp[j - 1] - A[j])
                    Y = max(Y, dp[j - 1] + A[j])
                    ndp[j] = max(ndp[j - 1], X + A[j], Y - A[j])
                dp = ndp
                ans = max(ans, dp[N - 1])

            return ans

        i = A.index(min(A))
        A = A[i:] + A[:i]
        B = A[1:] + A[:1]
        return max(solve(A), solve(B))
