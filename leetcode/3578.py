class Solution:
    def countPartitions(self, nums: List[int], k: int) -> int:
        n = len(nums)
        MOD = 10**9 + 7

        @cache
        def dfs(index, prev_min, prev_max):
            if index >= n:
                return 1
            new_min = min(nums[index], prev_min)
            new_max = max(nums[index], prev_max)
            res = dfs(index + 1, nums[index], nums[index])
            if new_max - new_min <= k:
                res += dfs(index + 1, new_min, new_max)
            res = res % MOD
            return res

        res = dfs(1, nums[0], nums[0])
        return res
