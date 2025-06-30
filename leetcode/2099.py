class Solution:
    def maxSubsequence(self, nums: List[int], k: int) -> List[int]:
        arr = sorted(list(range(len(nums))), key=lambda x: nums[x], reverse=True)
        arr = sorted(arr[:k])
        return [nums[i] for i in arr]
