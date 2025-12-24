class Solution:
    def arrayNesting(self, nums: List[int]) -> int:
        seen = set()

        def dfs(u, res=1):
            seen.add(u)
            if nums[u] not in seen:
                return dfs(nums[u], res + 1)
            return res

        m = 0
        for i in range(len(nums)):
            if i not in seen:
                m = max(dfs(i), m)
        return m
