from collections import deque


def kMirror(k: int, n: int) -> int:

    def convert(cur, k):
        if not cur == cur[::-1]:
            return -1
        base10 = sum([int(c) * (k**i) for i, c in enumerate(cur)])
        base10_str = str(base10)
        return base10 if base10_str == base10_str[::-1] else -1

    def bfs(cur):
        res = []
        q = deque([cur])
        while q:
            tar = q.popleft()
            if (num := convert(tar, k)) > 0:
                print(tar)
                res.append(num)
            if len(res) >= n:
                break
            for i in range(k):
                if tar == "" and i == 0:
                    continue
                q.append(tar + str(i))

        return res

    res = bfs("")
    print(res)
    return sum(res)


res = kMirror(7, 17)
print(res)
