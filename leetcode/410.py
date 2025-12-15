class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:

        prefix = [0]
        for num in nums:
            prefix.append(prefix[-1] + num)

        n = len(nums)
        splits = [0] * k

        def dfs(cur, idx):
            if cur == n:
                if idx == k:
                    return max(splits)
                return float("inf")
            if idx >= k:
                return float("inf")

            res = float("inf")
            splits[idx] += nums[cur]
            res = min(res, dfs(cur + 1, idx))
            res = min(res, dfs(cur + 1, idx + 1))
            splits[idx] -= nums[cur]

            return res

        res = dfs(0, 0)
        return res
