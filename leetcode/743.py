import heapq
from collections import defaultdict
from typing import List


class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        # 1. 그래프 구성
        graph = defaultdict(list)
        for u, v, w in times:
            graph[u].append((v, w))

        # 2. 우선순위 큐 초기화: (소요시간, 노드)
        # 시작 노드 k까지의 시간은 0
        pq = [(0, k)]

        # 3. 거리 테이블 초기화
        # dist는 각 노드까지의 최단 시간을 저장합니다.
        dist = {}

        while pq:
            time, node = heapq.heappop(pq)

            # 이미 처리된 노드(더 짧은 경로가 발견된 경우)라면 스킵
            if node in dist:
                continue

            # 해당 노드까지의 최단 시간 확정
            dist[node] = time

            # 인접 노드 탐색
            for v, w in graph[node]:
                if v not in dist:
                    heapq.heappush(pq, (time + w, v))

        # 4. 결과 반환
        # 모든 노드(n개)에 신호가 도달했는지 확인
        if len(dist) == n:
            return max(dist.values())
        else:
            return -1
