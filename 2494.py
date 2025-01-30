from collections import defaultdict, deque
from typing import List

class Solution:
    def magnificentSets(self, n: int, edges: List[List[int]]) -> int:
        """
        Calculates the sum of the maximum distances within each connected component of a graph.

        Args:
            n: The number of nodes in the graph.
            edges: A list of edges, where each edge is a list [u, v] representing a connection
                   between node u and node v.

        Returns:
            The sum of the maximum distances within each connected component, or -1 if an odd cycle exists.
        """

        # UF is a dictionary for Union-Find, mapping each node to its parent node.
        # Nodes are considered in the same connected component if they have the same root.
        UF = {}

        def find(x):
            """Finds the root (representative) of the connected component containing node x."""
            if x not in UF:
                UF[x] = x  # Initialize x's root as itself if it's new
            if x != UF[x]:
                UF[x] = find(UF[x])  # Path compression: update x's parent to the root
            return UF[x]

        def union(x, y):
            """Merges the connected components of x and y by setting the root of x's component
             to point to the root of y's component."""
            root_x = find(x)
            root_y = find(y)
            UF[root_x] = root_y  # Merge the components by making root_y the parent of root_x

        def bfs(node):
            """Performs a BFS to determine the maximum distance within the connected component
            containing the provided node. Returns -1 if an odd cycle is detected."""
            q = deque([(node, 1)])  # Initialize queue with start node and its level
            seen = {node: 1}  # Keep track of visited nodes and their level
            max_level = 1  # Maximum level (distance from the starting node)
            
            while q:
                current, level = q.popleft()
                max_level = max(max_level, level)  # Update max_level
                for neighbor in graph[current]:
                    if neighbor not in seen:
                        seen[neighbor] = level + 1
                        q.append((neighbor, level + 1))
                    elif seen[neighbor] == level:
                        # Odd cycle detected, return -1
                        return -1
            return max_level

        # Build adjacency list representation of graph
        graph = defaultdict(list)
        for start, end in edges:
            graph[start].append(end)
            graph[end].append(start)
            union(start, end)  # Construct connected components using union-find

        max_group_distances = defaultdict(int) # key is root node of the connected component, value is max distance within this component
        
        # Perform BFS on each node. If no odd cycles, update largest distances of the connected components.
        for i in range(1, n + 1):
            max_dist = bfs(i)
            if max_dist == -1:
                return -1  # Odd cycle detected
            root = find(i)
            max_group_distances[root] = max(max_group_distances[root], max_dist)

        return sum(max_group_distances.values())