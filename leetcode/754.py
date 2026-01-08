class Solution:
    def reachNumber(self, target: int) -> int:

        bound = abs(target) * 2

        def in_boundary(num):
            return -bound < num < bound

        def bfs(cur=0):
            q = deque([(cur, 0)])
            while q:
                tar, step = q.popleft()
                if tar == target:
                    return step - 1
                if in_boundary(tar + step):
                    q.append((tar + step, step + 1))
                if in_boundary(tar - step):
                    q.append((tar - step, step + 1))

            return -1

        # @cache
        # def dfs(cur=0, steps=1):
        #     if not (-bound < cur < bound):
        #         return float("inf")
        #     if cur == target:
        #         return 0

        #     res = float("inf")
        #     res = min(res, 1 + dfs(cur + steps, steps + 1))
        #     res = min(res, 1 + dfs(cur - steps, steps + 1))
        #     return res

        temp = bfs()
        return temp
