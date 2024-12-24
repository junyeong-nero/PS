from collections import deque
from typing import List

class Solution:
    def minimumDiameterAfterMerge(self, edges1: List[List[int]], edges2: List[List[int]]) -> int:

        def help(edges):
            n = len(edges)
            d = [[] for _ in range(n + 1)]
            for u, v in edges:
                d[u].append(v)
                d[v].append(u)

            leaves = [i for i in range(n + 1) if len(d[i]) == 1]

            q = deque(leaves)
            level = 0
            visited = set()
            arr = []
            while q:
                n = len(q)
                for _ in range(n):
                    tar = q.popleft()
                    visited.add(tar)

                    check = False
                    for nei in d[tar]:
                        if nei in visited:
                            continue
                        q.append(nei)
                        check = True
                    if check:
                        arr.append(level + 1)
                
                level += 1
            
            return level

        if not edges1 and not edges2:
            return 1
        if not edges1:
            return help(edges2)
        if not edges2:
            return help(edges1)
        a, b = help(edges1), help(edges2)
        return a + b - 1