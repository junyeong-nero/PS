class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        
        n = len(nums)
        nums = sorted(nums)

        res = float("-inf")
        for i in range(n // 2 + 1):
            # print(nums[i], nums[n - 1 - i])
            res = max(res, nums[i] + nums[n - 1 - i])

        return res
            