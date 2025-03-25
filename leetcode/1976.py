class Solution:
    def countPaths(self, n: int, roads: List[List[int]]) -> int:
        
        d = defaultdict(dict)
        for u, v, time in roads:
            d[u][v] = time
            d[v][u] = time
        # print(d)

        paths = dict()
        min_cost = float("inf")
        visited = {0}

        @cache
        def dfs(cur, cost):
            nonlocal min_cost, visited
            if cost > min_cost:
                return
            if cur == n - 1:
                paths[cost] = paths.get(cost, 0) + 1
                min_cost = min(min_cost, cost)
                return

            for node in d[cur]:
                if node in visited:
                    continue
                visited |= {node}
                dfs(node, cost + d[cur][node])

        dfs(0, 0)
        return paths[min_cost]
            
            