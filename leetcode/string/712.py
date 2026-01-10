class Solution:
    def minimumDeleteSum(self, s1: str, s2: str) -> int:
        m, n = len(s1), len(s2)

        s1 = [ord(c) for c in s1]
        s2 = [ord(c) for c in s2]

        @cache
        def dfs(i, j):
            if i == m:
                return sum([s2[x] for x in range(j, n)])
            if j == n:
                return sum([s1[x] for x in range(i, m)])

            res = float("inf")
            if s1[i] == s2[j]:
                res = min(res, dfs(i + 1, j + 1))
            else:
                res = min(res, s1[i] + dfs(i + 1, j))
                res = min(res, s2[j] + dfs(i, j + 1))

            return res

        temp = dfs(0, 0)
        return temp
