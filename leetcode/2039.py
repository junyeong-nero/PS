class Solution:
    def networkBecomesIdle(self, edges: List[List[int]], patience: List[int]) -> int:
        
        n = len(patience)
        tree = defaultdict(list)
        for u, v in edges:
            tree[u].append(v)
            tree[v].append(u)
        # print(tree)

        q = deque([(0, 0)])
        visited = [False] * n
        dist = [float('inf')] * n

        while q:
            tar, d = q.popleft()
            if visited[tar]:
                continue
            visited[tar], dist[tar] = True, d
            # print(tar, d)

            for node in tree[tar]:
                q.append((node, d + 1))

        # print(dist)
        res = 0
        for i in range(1, n):
            first = dist[i] * 2
            count = (first - 1) // patience[i]
            res = max(res, first + count * patience[i] + 1)

        return res
            