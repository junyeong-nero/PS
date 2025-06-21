class Solution:
    def maxDistance(self, s: str, k: int) -> int:
        counter = Counter(s)
        n = len(s)

        dirs = [1, 0, -1, 0, 1]
        map_ = {
            "N": 0,
            "S": 2,
            "W": 1,
            "E": 3,
        }

        res = k

        x, y = 0, 0
        for i, c in enumerate(s):
            dx, dy = dirs[map_[c]], dirs[map_[c] + 1]
            x, y = x + dx, y + dy
            flag = (x > 0, y > 0)
            temp = abs(x) + abs(y) + min(n - i - 1, k)
            res = max(res, temp)

        # print(res)
        return res
            