class Solution:
    def maximumProduct(self, nums: List[int], m: int) -> int:
        if m == 1:
            return max(map(lambda x: x**2, nums))

        n = len(nums)
        prefix_min, prefix_max = [float("inf")], [float("-inf")]
        for num in nums:
            prefix_min.append(min(num, prefix_min[-1]))
            prefix_max.append(max(num, prefix_max[-1]))

        res = float("-inf")
        for i in range(m - 1, n):
            res = max(
                res, nums[i] * prefix_min[i - m + 2], nums[i] * prefix_max[i - m + 2]
            )

        return res
