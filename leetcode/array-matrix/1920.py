class Solution:
    def buildArray(self, nums: List[int]) -> List[int]:

        n = len(nums)
        arr = [nums[nums[i]] for i in range(n)]
        return arr
