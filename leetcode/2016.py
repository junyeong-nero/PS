class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        n = len(nums)
        res = -1
        max_value = nums[-1]

        for j in range(n - 1, -1, -1):
            if nums[j] >= max_value:
                max_value = nums[j]
            else:
                res = max(res, max_value - nums[j])

        return res