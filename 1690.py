class Solution:
    def stoneGameVII(self, stones: List[int]) -> int:
        q = deque(stones)
        total = sum(stones)
        
        def dfs(turn, left, value):
            res = value
            if not q:
                return res

            temp = q.popleft()
            res = min(res, dfs(-turn, left - temp, value + turn * (left - temp)))
            q.appendleft(temp)

            temp = q.pop()
            res = min(res, dfs(-turn, left - temp, value + turn * (left - temp)))
            q.append(temp)

            return res

        return dfs(-1, total, 0)