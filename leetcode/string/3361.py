class Solution:
    def shiftDistance(
        self, s: str, t: str, nextCost: List[int], previousCost: List[int]
    ) -> int:
        # 1. 누적 합(Prefix Sum) 계산
        # next_sum[i]: 인덱스 0부터 i-1까지 nextCost의 합
        next_sum = [0] * 27
        # prev_sum[i]: 인덱스 0부터 i-1까지 previousCost의 합
        prev_sum = [0] * 27

        for i in range(26):
            next_sum[i + 1] = next_sum[i] + nextCost[i]
            prev_sum[i + 1] = prev_sum[i] + previousCost[i]

        total_next_cost = next_sum[26]
        total_prev_cost = prev_sum[26]

        # 2. 모든 알파벳 쌍(u -> v)에 대한 최소 비용 미리 계산 (26x26)
        min_cost_matrix = [[0] * 26 for _ in range(26)]

        for u in range(26):
            for v in range(26):
                if u == v:
                    min_cost_matrix[u][v] = 0
                    continue

                # --- 정방향 비용 (nextCost 사용) ---
                if u < v:
                    # u -> v (중간에 끊김 없음)
                    cost_forward = next_sum[v] - next_sum[u]
                else:
                    # u -> 25 -> 0 -> v (한 바퀴 돎)
                    cost_forward = (total_next_cost - next_sum[u]) + next_sum[v]

                # --- 역방향 비용 (previousCost 사용) ---
                # previousCost[i]는 i -> i-1 로 가는 비용
                if u > v:
                    # u -> v (내려가는 방향, 끊김 없음)
                    # 필요한 비용 인덱스: u, u-1, ..., v+1
                    # 누적합 범위: [v+1, u]
                    cost_backward = prev_sum[u + 1] - prev_sum[v + 1]
                else:
                    # u -> 0 -> 25 -> v (거꾸로 한 바퀴 돎)
                    # 전체 역방향 비용 - (v에서 u로 역방향으로 가는 비용)
                    # v -> u 역방향 비용 구간: [u+1, v]
                    gap_cost = prev_sum[v + 1] - prev_sum[u + 1]
                    cost_backward = total_prev_cost - gap_cost

                min_cost_matrix[u][v] = min(cost_forward, cost_backward)

        # 3. 실제 문자열 비용 계산
        total_cost = 0
        for char_s, char_t in zip(s, t):
            u = ord(char_s) - ord("a")
            v = ord(char_t) - ord("a")
            total_cost += min_cost_matrix[u][v]

        return total_cost
