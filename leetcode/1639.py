from collections import defaultdict
from typing import List
from functools import cache
from bisect import bisect_right

class Solution:
    def numWays(self, words: List[str], target: str) -> int:
        n, MOD = len(target), 10**9 + 7
        d = defaultdict(dict)

        for word in words:
            for i, c in enumerate(word):
                if i not in d[c]:
                    d[c][i] = 0
                d[c][i] += 1
        # print(d)

        @cache
        def dfs(index, k):
            if index == n:
                return 1
            temp = 0
            c = target[index]
            for i in d[c].keys():
                if i <= k:
                    continue
                temp += d[c][i] * dfs(index + 1, i)
            temp = temp % MOD
            return temp

        return dfs(0, -1)