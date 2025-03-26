class Solution:
    def maximalPathQuality(self, values: List[int], edges: List[List[int]], maxTime: int) -> int:
        
        graph = defaultdict(list)
        for u, v, time in edges:
            graph[u].append((v, time))
            graph[v].append((u, time))
        # print(graph)

        n = len(values)
        visited = [False] * n
        visited[0] = True
        
        max_cost = -1   
   
        def dfs(cur, time, cost):
            if time > maxTime:
                return
            if cur == 0:
                nonlocal max_cost
                max_cost = max(max_cost, cost)

            for node, t in graph[cur]:
                new_cost = cost if visited[node] else cost + values[node]

                temp, visited[node] = visited[node], True
                dfs(node, time + t, new_cost)
                visited[node] = temp

        dfs(0, 0, values[0])
        return max_cost