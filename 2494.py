class Solution:
    def magnificentSets(self, n: int, edges: List[List[int]]) -> int:
        
        tree = defaultdict(list)
        for u, v in edges:
            tree[u].append(v)
            tree[v].append(u)
        # print(tree)
        
        visited = {}
        def bfs(cur):
            q = deque([cur])
            visited = {}
            level = 0
            while q:
                # print(q)
                for _ in range(len(q)):
                    tar = q.popleft()
                    visited[tar] = level
                    for node in tree[tar]:
                        if node in visited:
                            if abs(visited[node] - level) != 1:
                                level = float('inf')
                                break
                        else:
                            q.append(node)
                level += 1
            # print(cur, level, visited)
            return level               

        res = -1
        for i in range(1, n + 1):
            visited = {}
            temp = bfs(i)
            if temp == float('inf'):
                continue
            res = max(res, temp)

        return res