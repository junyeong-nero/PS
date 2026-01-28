class Solution:
    def maxAlternatingSum(self, nums: List[int]) -> int:
        n = len(nums)
        nums = map(lambda x: x**2, nums)
        nums = sorted(nums)

        res = 0
        i, j = 0, n - 1
        while i <= j:
            if i == j:
                res += nums[i]
                break

            res += nums[j] - nums[i]
            i += 1
            j -= 1

        return res
