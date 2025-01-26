from typing import List, Tuple
from functools import lru_cache

class Solution:
    def maximumInvitations(self, A: List[int]) -> int:
        n = len(A)
        depth = [-1] * n  # depth[i]: depth of node i; -1 means unvisited
        reverse_graph = [[] for _ in range(n)]  # reverse_graph[i]: list of nodes pointing to i
        for i, neighbor in enumerate(A):
            reverse_graph[neighbor].append(i)

        @lru_cache(None)
        def calculate_depth(node: int) -> int:
            """Calculates the depth of a node using DFS."""
            if depth[node] != -1:
                return depth[node]
            max_child_depth = 0
            for child in reverse_graph[node]:
                max_child_depth = max(max_child_depth, calculate_depth(child))
            depth[node] = 1 + max_child_depth
            return depth[node]

        max_cycle_size = 0  # Maximum cycle size found
        max_free_component_size = 0  # Maximum free component size (not in cycles)

        for i in range(n):
            if depth[i] != -1:  # Skip if already visited
                continue
            if A[A[i]] == i:  # Handle pairs connected by edges A[i] -> A[A[i]] -> i
                depth[i] = depth[A[i]] = 0
                arm_length_i = 0
                arm_length_neighbor = 0
                
                for neighbor in reverse_graph[i]:
                    if neighbor != A[i]:
                        arm_length_i = max(arm_length_i, calculate_depth(neighbor))

                for neighbor in reverse_graph[A[i]]:
                    if neighbor != i:
                         arm_length_neighbor = max(arm_length_neighbor, calculate_depth(neighbor))

                max_free_component_size += arm_length_i + arm_length_neighbor + 2

        def find_cycle_info(node: int) -> Tuple[int, int, bool]:
            """
            Finds cycle information using DFS: entry node, depth, is_cycle_visited
            """
            if depth[node] != -1: # Visited this node again - entry of the cycle
                return node, depth[node], False
            depth[node] = 0
            entry_node, cycle_depth, cycle_visited = find_cycle_info(A[node])
            if cycle_visited: # Outside the cycle - don't increment depth
                return entry_node, cycle_depth, True 
            depth[node] = 1 + cycle_depth # node is in cycle
            return entry_node, depth[node], node == entry_node # Check if current node is the entry of the cycle
       

        for i in range(n):
            if depth[i] != -1:  # Skip already visited
                continue
            entry, cycle_len, is_cycle = find_cycle_info(i)
            if is_cycle:
                max_cycle_size = max(max_cycle_size, cycle_len)

        return max(max_cycle_size, max_free_component_size)