class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:

        graph = defaultdict(list)
        for u, v, w in times:
            graph[u].append((v, w))

        q = deque([(k, 0)])
        arrival_time = [float("inf")] * (n + 1)
        arrival_time[0] = 0

        while q:
            tar, cur = q.popleft()
            arrival_time[tar] = min(arrival_time[tar], cur)
            for node, time in graph[tar]:
                if arrival_time[node] <= cur + time:
                    continue
                q.append((node, cur + time))

        # print(arrival_time)
        res = max(arrival_time)
        return -1 if res == float("inf") else res
