class Solution:
    def maxSumDivThree(self, nums: List[int]) -> int:
        n = len(nums)
        res = 0
        for i in range(n, 0, -1):
            arr = list(combinations(nums, i))
            temp = max([0] + [sum(elem) for elem in arr if sum(elem) % 3 == 0])
            res = max(res, temp)

        return res
