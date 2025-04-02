class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        n = len(nums)
        res, max_distance, max_value = 0, 0, 0
        for num in nums:
            res = max(res, max_distance * num)
            max_distance = max(max_distance, max_value - num)
            max_value = max(num, max_value)
        
        return res