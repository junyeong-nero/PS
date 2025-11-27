class Solution:
    def maxSubarraySum(self, nums: List[int], k: int) -> int:
        n = len(nums)
        value = n // k

        d = defaultdict(int)
        res = -float("inf")
        for i in range(value):
            d[i] = sum(nums[: k * (i + 1)])
            res = max(res, d[i])

        for i in range(n - k):
            for j in range(value):
                if (i + k * (j + 1)) >= n:
                    continue
                d[j] -= nums[i]
                d[j] += nums[i + k * (j + 1)]
                res = max(res, d[j])

        return res
