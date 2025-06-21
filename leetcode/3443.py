class Solution:
    def maxDistance(self, s: str, k: int) -> int:
        counter = Counter(s)
        n = len(s)

        map_ = {
            "N": 0,
            "S": 2,
            "W": 1,
            "E": 3,
        }

        def dfs(x, y, index, left):
            res = abs(x) + abs(y)
            if index >= n:
                return res
            dirs = [1, 0, -1, 0, 1]
            i = map_[s[index]]
            dx, dy = dirs[i], dirs[i + 1]
            res = max(res, dfs(x + dx, y + dy, index + 1, left))
            if left > 0:
                for i in range(4):
                    dx, dy = dirs[i], dirs[i + 1]
                    res = max(res, dfs(x + dx, y + dy, index + 1, left - 1))
            
            return res

        res = dfs(0, 0, 0, k)
        return res
            