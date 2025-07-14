class Solution:
    def countPaths(self, n: int, roads: List[List[int]]) -> int:
        MOD = 10**9 + 7

        graph = defaultdict(list)
        for u, v, time in roads:
            graph[u].append((time, v))
            graph[v].append((time, u))
        # print(d)

        dist = [float("inf")] * n
        dist[0] = 0

        ways = [0] * n
        ways[0] = 1

        q = []
        heappush(q, (0, 0))

        while q:
            cur_time, node = heappop(q)
            for time, nei in graph[node]:
                new_time = cur_time + time
                if new_time < dist[nei]:
                    dist[nei] = new_time
                    ways[nei] = ways[node]
                    heappush(q, (new_time, nei))
                elif new_time == dist[nei]:
                    ways[nei] = (ways[nei] + ways[node]) % MOD

        return ways[n - 1]
