from collections import *
from typing import *
from bisect import *


class Solution:
    def maximumTotalDamage(self, power: List[int]) -> int:
        counter = Counter(power)
        keys = sorted(list(counter.keys()))
        n = len(keys)

        # def dfs(index=0, lower_bound=-1):
        #     temp = 0
        #     for i in range(index, n):
        #         key = keys[i]
        #         if key <= lower_bound:
        #             continue
        #         temp = max(temp, key * counter[key] + dfs(i + 1, keys[i] + 2))
        #     return temp

        dp = [0] * n
        for i in range(n):
            key = keys[i]
            bound = bisect_left(keys, key - 2)
            dp[i] = max(dp[i], key * counter[key] + max(dp[:bound] + [0]))

        # print(dp)
        return max(dp)
