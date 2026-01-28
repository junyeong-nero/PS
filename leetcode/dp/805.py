class Solution:
    def splitArraySameAverage(self, nums: List[int]) -> bool:

        total = sum(nums)
        nums.sort()
        n = len(nums)

        @cache
        def dfs(i, k, target):
            if k == 0:
                return target == 0
            if i == n or target < 0 or k < 0:
                return False
            return dfs(i + 1, k - 1, target - nums[i]) or dfs(i + 1, k, target)

        for k in range(1, n // 2 + 1):
            if k * total % n == 0:
                target = k * total // n
                if dfs(0, k, target):
                    return True

        return False
