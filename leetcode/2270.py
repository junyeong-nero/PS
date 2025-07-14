class Solution:
    def waysToSplitArray(self, nums: List[int]) -> int:
        left = 0
        right = sum(nums)
        res = 0
        for num in nums[:-1]:
            left += num
            right -= num
            if left >= right:
                res += 1

        return res
