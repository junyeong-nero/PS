class Solution:
    def waysToReachStair(self, k: int) -> int:

        def get_position(cur, jump):
            return cur + 2**jump

        res = 0
        q = deque([(1, 0, True)])
        d = defaultdict(int)

        while q:
            # print(q)
            cur, jump, is_backward = q.popleft()
            d[cur] += 1

            next_ = get_position(cur, jump)
            if next_ <= 2 * k + 1:
                q.append((next_, jump + 1, True))
            if is_backward and cur > 0:
                q.append((cur - 1, jump, False))

        # print(d)
        return d[k]
