from collections import defaultdict
from typing import List


class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        d = defaultdict(dict)

        def dfs(idx, tar):
            if tar in d[idx]:
                return d[idx][tar]
            if idx >= len(nums):
                return 1 if tar == 0 else 0

            temp = dfs(idx + 1, tar + nums[idx]) + dfs(idx + 1, tar - nums[idx])
            d[idx][tar] = temp
            return temp

        return dfs(0, target)
