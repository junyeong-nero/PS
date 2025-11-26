class Solution:
    def waysToReachStair(self, k: int) -> int:

        def get_position(cur, jump):
            return cur + 2**jump

        res = 0
        q = deque([(1, 0), (0, 0)])

        while q:
            cur, jump = q.popleft()
            if cur == k:
                res += 1
            if cur > k:
                continue

            temp = get_position(cur, jump)
            q.append((temp, jump + 1))
            q.append((temp - 1, jump + 1))

        return res
