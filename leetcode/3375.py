class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        temp = min(nums)
        if temp < k:
            return -1
        res = len(set(nums)) 
        if temp == k:
            res -= 1
        return res