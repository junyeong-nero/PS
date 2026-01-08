class Solution:
    def reachNumber(self, target: int) -> int:

        bound = abs(target) * 2

        @cache
        def dfs(cur=0, steps=1):
            if not (-bound < cur < bound):
                return float("inf")
            if cur == target:
                return 0

            res = float("inf")
            res = min(res, 1 + dfs(cur + steps, steps + 1))
            res = min(res, 1 + dfs(cur - steps, steps + 1))
            return res

        temp = dfs()
        return temp
