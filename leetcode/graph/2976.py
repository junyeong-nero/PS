from typing import List


class Solution:
    def minimumCost(
        self,
        source: str,
        target: str,
        original: List[str],
        changed: List[str],
        cost: List[int],
    ) -> int:
        INF = 10**18
        N = 26

        # dist[u][v] = min cost to convert chr(u+'a') -> chr(v+'a')
        dist = [[INF] * N for _ in range(N)]
        for i in range(N):
            dist[i][i] = 0

        # Apply direct conversion rules (keep the cheapest one per edge)
        for o, c, w in zip(original, changed, cost):
            u = ord(o) - ord("a")
            v = ord(c) - ord("a")
            if w < dist[u][v]:
                dist[u][v] = w

        # Floyd–Warshall on 26 nodes
        for k in range(N):
            dk = dist[k]
            for i in range(N):
                ik = dist[i][k]
                if ik == INF:
                    continue
                di = dist[i]
                for j in range(N):
                    kj = dk[j]
                    if kj == INF:
                        continue
                    nd = ik + kj
                    if nd < di[j]:
                        di[j] = nd

        # Sum minimal costs for each character position
        ans = 0
        for s, t in zip(source, target):
            if s == t:
                continue
            u = ord(s) - ord("a")
            v = ord(t) - ord("a")
            d = dist[u][v]
            if d == INF:
                return -1
            ans += d

        return ans


# from typing import List
# from collections import defaultdict
# import heapq
# import math


class Solution:
    def minimumCost(
        self,
        source: str,
        target: str,
        original: List[str],
        changed: List[str],
        cost: List[int],
    ) -> int:
        # 1) 그래프 구성: 26 letters nodes
        g = defaultdict(list)
        for o, c, w in zip(original, changed, cost):
            g[o].append((c, w))

        letters = [chr(ord("a") + i) for i in range(26)]
        src_set = set(source)

        # 2) 각 source에 등장하는 시작 문자에 대해 다익스트라 1번씩
        dist = {s: {ch: math.inf for ch in letters} for s in src_set}

        def dijkstra(start: str):
            d = dist[start]
            d[start] = 0
            pq = [(0, start)]  # (cost, node)

            while pq:
                cur_cost, u = heapq.heappop(pq)
                if cur_cost != d[u]:
                    continue
                for v, w in g[u]:
                    nc = cur_cost + w
                    if nc < d[v]:
                        d[v] = nc
                        heapq.heappush(pq, (nc, v))

        for s in src_set:
            dijkstra(s)

        # 3) position-wise 비용 합산
        ans = 0
        for s_ch, t_ch in zip(source, target):
            if s_ch == t_ch:
                continue
            c = dist[s_ch][t_ch]
            if c == math.inf:
                return -1
            ans += c

        return ans
