class Solution:
    def lexicographicallySmallestArray(self, nums: List[int], limit: int) -> List[int]:
        n = len(nums)
        i = 0
        while i < n:
            idx = i
            for j in range(i + 1, n):
                diff = nums[i] - nums[j]
                if diff > 0 and diff <= limit:
                    if nums[j] < nums[idx]:
                        idx = j
            if idx != i:
                nums[i], nums[idx] = nums[idx], nums[i]
                i -= 1
            i += 1

        return nums