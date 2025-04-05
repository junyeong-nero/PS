
class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:

        n = len(nums)

        @cache
        def func(cur, value):
            if cur >= n:
                return value
            res = value
            for i in range(cur, n):
                res += func(i + 1, value ^ nums[i])
            return res
            
        return func(0, 0)