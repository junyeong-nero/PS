from typing import List

class Solution:
    def findScore(self, nums: List[int]) -> int:
        n = len(nums)
        marked = [False for i in range(n)]
        nums = [(nums[i], i) for i in range(n)]
        nums = sorted(nums)
        
        res = 0
        for i in range(n):
            idx = nums[i][1]
            if marked[idx]:
                continue
            res += nums[i][0]
            marked[idx] = True
            if idx + 1 < n: marked[idx + 1] = True
            if idx - 1 >= 0: marked[idx - 1] = True

        return res