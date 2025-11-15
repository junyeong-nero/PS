class Solution:
    def minOperations(self, nums: List[int]) -> int:
        n = len(nums)
        if gcd(*nums) != 1:
            return -1

        arr = nums[:]
        count = 0
        while 1 not in arr:
            temp = [arr[0]] + [gcd(arr[i - 1], arr[i]) for i in range(1, n)]
            arr = temp
            count += 1

        return n - nums.count(1) + max(0, count - 1)
