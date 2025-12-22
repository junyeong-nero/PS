class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:

        m, n = len(strs), len(strs[0])

        def dfs(s, index=0, last_index=None, history=[]):
            if index >= len(s):
                return [tuple(history)]

            cur = s[index]
            last = s[last_index] if last_index is not None else "a"
            res = []

            # pass
            res += dfs(s, index + 1, last_index, history + [index])

            # select
            if cur >= last:
                res += dfs(s, index + 1, index, history)

            return res

        res = set(dfs(strs[0]))
        for s in strs[1:]:
            temp = set(dfs(s))
            res = res & temp

        # print(res)
        res = min(res, key=lambda x: len(x))
        return len(res)
