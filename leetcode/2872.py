from collections import defaultdict, deque
from typing import List

class Solution:
    
    # TLE at 712/736
    def maxKDivisibleComponents(self, n: int, edges: List[List[int]], values: List[int], k: int) -> int:

        g = defaultdict(set)
        for u, v in edges:
            g[u].add(v)
            g[v].add(u)

        def sum_graphs(root):
            q = deque([root])
            visited = set()
            res = 0
            while q:
                
                tar = q.popleft()
                res += values[tar]
                visited.add(tar)

                for child in g[tar]:
                    if child in visited:
                        continue
                    q.append(child)

            return res

        count = 0
        for u, v in edges:
            g[u].remove(v)
            g[v].remove(u)
            
            a, b = sum_graphs(u), sum_graphs(v)
            if a % k == 0 and b % k == 0:
                # print(u, v)
                # print(a, b)
                count += 1
            else:
                g[u].add(v)
                g[v].add(u)

        return count + 1
    
    def maxKDivisibleComponents(self, n: int, edges: List[List[int]], values: List[int], k: int) -> int:
        g = defaultdict(set)
        for u, v in edges:
            g[u].add(v)
            g[v].add(u)

        def dfs(node, parent):
            total = values[node]
            for child in g[node]:
                if child == parent:
                    continue
                total += dfs(child, node)
            subtree_sum[node] = total
            return total

        subtree_sum = {}
        dfs(0, -1)

        count = 0
        for u, v in edges:
            if subtree_sum[u] % k == 0 and (subtree_sum[0] - subtree_sum[u]) % k == 0:
                count += 1

        return count + 1
    
    
    # TLE at 612/736
    def maxKDivisibleComponents(self, n: int, edges: List[List[int]], values: List[int], k: int) -> int:

        def _sum(root, visited = set()):
            temp = values[root]
            visited.add(root)
            for u, v in edges:
                if u == root and v not in visited:
                    temp += _sum(v, visited)
                if v == root and u not in visited:
                    temp += _sum(u, visited)
            return temp

        ignore = set()

        @cache
        def dfs(total):
            temp = 0
            for i, (u, v) in enumerate(edges):
                if i in ignore:
                    continue
                sub = _sum(u, set({v}))
                if sub % k == 0 and (total - sub) % k == 0:
                    ignore.add(i)
                    temp = max(temp, 1 + dfs(total))
            return temp
        
        return dfs(sum(values)) + 1
    
    def maxKDivisibleComponents(self, n, edges, values, k) -> int:
        if n <= 1:
            return 1

        count = 0

        # Build adjacency map
        graph = defaultdict(set)
        for u, v in edges:
            graph[u].add(v)
            graph[v].add(u)

        # Initialize queue with leaf nodes
        queue = deque(node for node, neighbors in graph.items() if len(neighbors) == 1)

        # Process nodes layer by layer
        while queue:
            node = queue.popleft()

            if not graph[node]:
                continue

            parent = next(iter(graph[node]))
            graph[parent].remove(node)
            graph[node].clear()

            # Check divisibility and update counts or propagate values
            if values[node] % k == 0:
                count += 1
            else:
                values[parent] += values[node]

            # Add new leaves to the queue
            if len(graph[parent]) == 1:
                queue.append(parent)

        # Check if the root node forms a valid component
        if values[parent] % k == 0:
            count += 1

        return count
