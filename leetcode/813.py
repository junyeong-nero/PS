class Solution:
    def largestSumOfAverages(self, nums: List[int], k: int) -> float:
        
        def avg(arr):
            return sum(arr) / len(arr)

        n = len(nums)
        d = dict()

        def func(index, k):
            if (index, k) in d:
                return d[(index, k)]
            if k == 1:
                return avg(nums[index:])
            res = 0
            for i in range(index + 1, n):
                prefix = nums[index:i]
                res = max(res, avg(prefix) + func(i, k - 1))
            
            d[(index, k)] = res
            return res
        
        return func(0, k)
            