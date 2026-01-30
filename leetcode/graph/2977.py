from typing import List
from collections import defaultdict

class Solution:
    def minimumCost(self, source: str, target: str, original: List[str], changed: List[str], cost: List[int]) -> int:
        # 1. 고유 문자열 인덱싱 및 거리 행렬 초기화
        nodes = list(set(original) | set(changed))
        node_to_idx = {s: i for i, s in enumerate(nodes)}
        num_nodes = len(nodes)
        
        # 최단 거리 행렬 (Floyd-Warshall용)
        dist = [[float('inf')] * num_nodes for _ in range(num_nodes)]
        for i in range(num_nodes):
            dist[i][i] = 0
            
        for u, v, w in zip(original, changed, cost):
            u_idx, v_idx = node_to_idx[u], node_to_idx[v]
            dist[u_idx][v_idx] = min(dist[u_idx][v_idx], w)
            
        # 2. Floyd-Warshall로 모든 쌍 최단 경로 계산
        for k in range(num_nodes):
            for i in range(num_nodes):
                if dist[i][k] == float('inf'): continue
                for j in range(num_nodes):
                    if dist[i][j] > dist[i][k] + dist[k][j]:
                        dist[i][j] = dist[i][k] + dist[k][j]

        # 3. 효율적인 패턴 매칭을 위한 준비
        # 길이에 따라 original 패턴들을 분류해둡니다.
        patterns_by_len = defaultdict(list)
        for s in nodes:
            patterns_by_len[len(s)].append(s)
        
        unique_lengths = sorted(patterns_by_len.keys())
        n = len(source)
        dp = [float('inf')] * (n + 1)
        dp[0] = 0

        # 4. DP 진행
        for i in range(n):
            if dp[i] == float('inf'):
                continue
            
            # Case 1: 현재 문자가 동일한 경우 (변환 불필요, 비용 0)
            if source[i] == target[i]:
                dp[i + 1] = min(dp[i + 1], dp[i])
            
            # Case 2: original/changed에 정의된 패턴으로 변환
            for l in unique_lengths:
                if i + l > n:
                    break
                
                src_sub = source[i:i + l]
                trg_sub = target[i:i + l]
                
                if src_sub in node_to_idx and trg_sub in node_to_idx:
                    u, v = node_to_idx[src_sub], node_to_idx[trg_sub]
                    if dist[u][v] != float('inf'):
                        dp[i + l] = min(dp[i + l], dp[i] + dist[u][v])
                        
        return dp[n] if dp[n] != float('inf') else -1

class Solution:
    def minimumCost(
        self,
        source: str,
        target: str,
        original: List[str],
        changed: List[str],
        cost: List[int],
    ) -> int:

        # abcdefgh
        # acdeefgh
        # acdeethh
        # acdeeghh

        # 1. disjoint substring.
        #    source[i] -> target[i] 로 변환 되어야 함, 인덱스가 겹칠 수 없음.
        # 2. identical indexing
        #

        d = defaultdict(list)
        for i in range(len(original)):
            d[original[i]].append((changed[i], cost[i]))

        n = len(source)
        m = max(map(len, original))
        diff_indices = [i for i in range(n) if source[i] != target[i]]

        @cache
        def convert(a, b):
            if a == b:
                return 0
            if not d[a]:
                return float("inf")

            q = [(0, a)]
            while q:
                cost, tar = heappop(q)
                if tar == b:
                    return cost

                for text, dcost in d[tar]:
                    heappush(q, (cost + dcost, text))

            return float("inf")

        @cache
        def dfs(cur, cost):

            if cur >= n:
                return cost

            res = float("inf")
            for l in range(1, m + 1):
                if cur + l > n:
                    continue

                src = source[cur : cur + l]
                trg = target[cur : cur + l]

                dcost = convert(src, trg)
                if dcost == float("inf"):
                    continue

                res = min(res, dfs(cur + l, cost + dcost))

            return res

        res = dfs(0, 0)
        return -1 if res == float("inf") else res

