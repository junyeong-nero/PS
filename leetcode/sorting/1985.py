class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        nums = sorted(nums)
        n = len(nums)
        if n == 1:
            return 0

        res = float("inf")
        for i in range(n - k + 1):
            cur = nums[i + k - 1] - nums[i]
            res = min(res, cur)

        return res
