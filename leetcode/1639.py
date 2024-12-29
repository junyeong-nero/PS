from collections import defaultdict
from typing import List
from functools import cache

class Solution:
    def numWays(self, words: List[str], target: str) -> int:
        n, MOD = len(target), 10**9 + 7
        m = len(words[0])
        freq = [defaultdict(int) for _ in range(m)]

        # 각 열의 문자의 빈도수를 저장
        for word in words:
            for i, c in enumerate(word):
                freq[i][c] += 1

        @cache
        def dfs(index, pos):
            if index == n:
                return 1
            if pos >= m:
                return 0
            
            char = target[index]
            temp = 0

            # 현재 열에서 문자를 선택하는 경우
            if char in freq[pos]:
                temp += freq[pos][char] * dfs(index + 1, pos + 1)
            
            # 현재 열을 건너뛰는 경우
            temp += dfs(index, pos + 1)

            return temp % MOD

        return dfs(0, 0)
