class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        index = 0
        n = len(nums)
        i = 0
        while i < n:
            j = i + 1
            while j < n and nums[j] == nums[i]:
                j += 1
            nums[index] = nums[i]
            index += 1
            i = j

        return index
