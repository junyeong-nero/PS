class Solution:
    def findKDistantIndices(self, nums: List[int], key: int, k: int) -> List[int]:
        n = len(nums)
        res = [-1]
        for i, num in enumerate(nums):
            if num != key:
                continue
            temp = list(range(max(0, i - k, res[-1] + 1), min(n, i + k + 1)))
            res += temp

        return res[1:]
