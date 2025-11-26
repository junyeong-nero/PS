class Solution:
    def maxSumMinProduct(self, nums: List[int]) -> int:

        n = len(nums)
        MOD = 10**9 + 7
        prefix_sum = [0]
        for num in nums:
            prefix_sum.append(prefix_sum[-1] + num)

        # prefix_sum[i] : sum(nums[:i])

        res = 0
        for i in range(n):
            min_value = nums[i]
            for j in range(i + 1, n + 1):
                sum_value = prefix_sum[j] - prefix_sum[i]
                min_value = min(min_value, nums[j - 1])
                res = max(res, sum_value * min_value % MOD)

        return res
