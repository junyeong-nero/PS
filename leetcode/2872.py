from collections import defaultdict, deque
from typing import List

class Solution:
    
    # TLE at 717/736
    def maxKDivisibleComponents(self, n: int, edges: List[List[int]], values: List[int], k: int) -> int:
        g = defaultdict(set)
        for u, v in edges:
            g[u].add(v)
            g[v].add(u)

        def sum_graphs(root, visited):
            q = deque([root])
            res = 0
            while q:
                node = q.popleft()
                if node in visited:
                    continue
                res += values[node]
                visited.add(node)
                for child in g[node]:
                    if child not in visited:
                        q.append(child)
            return res

        count = 1
        for u, v in edges:
            g[u].remove(v)
            g[v].remove(u)
            
            visited_u, visited_v = set(), set()
            a, b = sum_graphs(u, visited_u), sum_graphs(v, visited_v)
            if a % k == 0 and b % k == 0:
                count += 1
            else:
                g[u].add(v)
                g[v].add(u)

        return count