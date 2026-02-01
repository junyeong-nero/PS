class Solution:
    def reachableNodes(self, n: int, edges: List[List[int]], restricted: List[int]) -> int:

        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        # print(graph)

        q = deque([0])
        visited = set()
        restricted = set(restricted)

        while q:
            
            tar = q.popleft()
            visited.add(tar)

            for node in graph[tar]:
                if node in visited:
                    continue
                if node in restricted:
                    continue
                q.append(node)

        return len(visited)

