class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        res = 0 
        for num in nums:
            digit = len(str(num))
            if digit % 2 == 0:
                res += 1
        return res