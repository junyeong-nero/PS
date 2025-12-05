class Solution:
    def repeatedStringMatch(self, a: str, b: str) -> int:
        m, n = len(a), len(b)

        def dfs(idx, count):
            # print(idx, count)
            p = len(b[idx:])

            res = float("inf")
            if idx == n:
                return count
            if idx + m <= n and a == b[idx : idx + m]:
                return dfs(idx + m, count + 1)
            if p <= m:
                temp = (count + 1) if a[:p] == b[idx:] else float("inf")
                res = min(res, temp)
            if count == 0:
                if b in a:
                    return 1
                for i in range(m):
                    tar = a[i:]
                    # print(tar, b[idx:idx + len(tar)])
                    if tar == b[idx : idx + len(tar)]:
                        res = min(res, dfs(idx + len(tar), count + 1))
            return res

        res = dfs(0, 0)
        return -1 if res == float("inf") else res
