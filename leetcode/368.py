class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        
        n = len(nums)
        nums.sort()
        res = []

        for i in range(n):
            arr = [nums[i]]
            for j in range(i + 1, n):
                if nums[j] % arr[-1] == 0:
                    arr.append(nums[j])
            if len(arr) > len(res):
                res = arr

        return res