from collections import defaultdict
from typing import List
from functools import cache
from bisect import bisect_right

class Solution:
    def numWays(self, words: List[str], target: str) -> int:
        n, MOD = len(target), 10**9 + 7
        d = defaultdict(list)

        for word in words:
            for i, c in enumerate(word):
                d[c].append(i)
        
        for key in d.keys():
            d[key] = sorted(d[key])

        @cache
        def dfs(index, k):
            if index == n:
                return 1
            
            temp = 0
            arr = d[target[index]]
            start = bisect_right(arr, k)
            for i in range(start, len(arr)):
                temp += dfs(index + 1, arr[i])
            temp = temp % MOD
            return temp

        return dfs(0, -1)