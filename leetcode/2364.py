
class Solution:
    def countBadPairs(self, nums: List[int]) -> int:
        n = len(nums)
        res = 0
        for i in range(n):
            for j in range(i + 1, n):
                if j - i != nums[j] - nums[i]:
                    res += 1
        return res