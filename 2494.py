class Solution:
    def magnificentSets(self, n: int, edges: List[List[int]]) -> int:
        
        tree = defaultdict(list)
        for u, v in edges:
            tree[u].append(v)
            tree[v].append(u)
        print(tree)
        
        visited = {}
        def dfs(cur, level=0):
            if cur in visited:
                if level < visited[cur]:
                    return float('inf') # cycle detected
                return visited[cur]
            visited[cur] = level
            temp = level
            for node in tree[cur]:
                temp = max(temp, dfs(node, level + 1))
            return temp + 1

        res = dfs(1, 0)
        return -1 if res == float('inf') else res