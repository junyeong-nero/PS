import heapq
from collections import defaultdict
from typing import List


class Solution:
    def minCost(self, n: int, edges: List[List[int]]) -> int:
        # 1. 그래프 구성 (인접 리스트)
        graph = defaultdict(list)
        for u, v, w in edges:
            graph[u].append((v, w))  # 정방향
            graph[v].append((u, w * 2))  # 역방향 (비용 2배)

        # 2. 다익스트라 알고리즘 준비
        # min_costs[i]는 0번 노드에서 i번 노드까지의 최소 비용을 저장 (DP 테이블 역할)
        min_costs = {i: float("inf") for i in range(n)}
        min_costs[0] = 0

        # 우선순위 큐: (현재까지의 비용, 현재 노드)
        pq = [(0, 0)]

        while pq:
            cur_cost, u = heapq.heappop(pq)

            # 최적화: 이미 처리된 비용보다 크다면 스킵 (Pruning)
            if cur_cost > min_costs[u]:
                continue

            # 목표 지점 도달 시 (우선순위 큐를 쓰므로 가장 먼저 나온 것이 최소 비용임)
            if u == n - 1:
                return cur_cost

            # 인접 노드 탐색
            for v, weight in graph[u]:
                next_cost = cur_cost + weight

                # 더 적은 비용으로 도달할 수 있다면 갱신 (Relaxation)
                if next_cost < min_costs[v]:
                    min_costs[v] = next_cost
                    heapq.heappush(pq, (next_cost, v))

        # 도달 불가능한 경우
        return -1 if min_costs[n - 1] == float("inf") else min_costs[n - 1]


# class Solution:
#     def minCost(self, n: int, edges: List[List[int]]) -> int:
#         # incomming edges -> outcomming edges at current node
#         # reversal edges cost doubled.
#         # travel cost from 0 to n - 1

#         switched = [False] * n
#         graph = defaultdict(dict)
#         for u, v, w in edges:
#             graph[u][v] = min(w, graph[u].get(v, float("inf")))
#             graph[v][u] = min(w * 2, graph[v].get(u, float("inf")))

#         visited = set()

#         @cache
#         def dfs(cur, cost=0):
#             if cur == n - 1:
#                 return cost
#             if cur in visited:
#                 return float("inf")

#             visited.add(cur)
#             res = float("inf")
#             for node, weight in graph[cur].items():
#                 res = min(res, dfs(node, cost + weight))

#             visited.remove(cur)
#             return res

#         res = dfs(0)
#         return -1 if res == float("inf") else res
