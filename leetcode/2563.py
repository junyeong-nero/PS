class Solution:
    def countFairPairs(self, nums: List[int], lower: int, upper: int) -> int:
        nums.sort()
        return sum([bisect_right(nums, upper - v, i + 1) - bisect_left(nums, lower - v, i + 1) for i,v in enumerate(nums)])