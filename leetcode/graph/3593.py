class Solution:
    def minIncrease(self, n: int, edges: List[List[int]], cost: List[int]) -> int:
        # 최적화 1: 딕셔너리 대신 리스트 배열 사용 (접근 속도 향상)
        graph = [[] for _ in range(n)]
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        # 최적화 2: Visited Set 대신 부모 노드(parent) 인자 활용
        def dfs(cur: int, parent: int):
            path_vals = []  # 자식들의 경로 합을 저장
            sum_cost = 0  # 현재 서브트리의 비용 합
            number_of_nodes = 0  # 조건에 맞는 노드 개수 합

            for node in graph[cur]:
                if node != parent:
                    # 재귀 호출
                    c_path, c_cost, c_nodes = dfs(node, cur)

                    path_vals.append(c_path)
                    sum_cost += c_cost
                    number_of_nodes += c_nodes

            # 리프 노드인 경우 (자식 경로가 없음)
            if not path_vals:
                return cost[cur], 0, 0

            # 최적화 3: 내장 함수 활용 (C로 구현되어 있어 빠름)
            max_p = max(path_vals)
            sum_p = sum(path_vals)
            count = len(path_vals)

            # 모든 자식의 경로 합을 max_p로 맞추기 위해 필요한 값 계산
            needed = (max_p * count) - sum_p

            if needed > 0:
                sum_cost += needed
                # 값이 변경된(증가된) 노드의 수 = 전체 자식 수 - 이미 최대값인 자식 수
                number_of_nodes += count - path_vals.count(max_p)

            return max_p + cost[cur], sum_cost, number_of_nodes

        # 루트 노드 0, 부모 -1로 시작
        _, _, res_nodes = dfs(0, -1)
        return res_nodes
