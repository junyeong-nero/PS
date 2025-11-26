class Solution:
    def waysToReachStair(self, k: int) -> int:

        def get_position(cur, jump):
            return cur + 2**jump

        @cache
        def dfs(cur, jump):
            # print(cur, jump)
            if cur > k:
                return 0
            res = 0
            if cur == k:
                res += 1

            temp = get_position(cur, jump)
            res += dfs(temp, jump + 1)
            res += dfs(temp - 1, jump + 1)
            return res

        res = dfs(0, 0) + dfs(1, 0)
        return res
