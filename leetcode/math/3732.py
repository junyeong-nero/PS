class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        nums = sorted(nums)
        const = 10**5
        candidates = [
            nums[-1] * nums[-2],
            nums[-1] * nums[0],
            nums[0] * nums[1],
        ]
        candidates = map(abs, candidates)
        return max(candidates) * const
