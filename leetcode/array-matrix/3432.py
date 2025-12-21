class Solution:
    def countPartitions(self, nums: List[int]) -> int:
        left, right = 0, sum(nums)
        res = 0
        for num in nums[:-1]:
            left += num
            right -= num
            if abs(right - left) % 2 == 0:
                res += 1
        return res
