class Solution:
    def largestSumOfAverages(self, nums: List[int], k: int) -> float:
        
        def avg(arr):
            return sum(arr) / len(arr)

        def func(cur, k):
            if k == 1:
                return avg(cur)
            res = 0
            for i in range(1, len(cur)):
                prefix = cur[:i]
                res = max(res, avg(prefix) + func(cur[i:], k - 1))
            
            return res
        
        return func(nums, k)
            