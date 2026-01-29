from typing import List


class Solution:
    def countVisitedNodes(self, edges: List[int]) -> List[int]:
        n = len(edges)
        ans = [0] * n
        state = [0] * n  # 0=unvisited, 1=visiting, 2=done
        idx = [-1] * n  # index in current stack when visiting

        for start in range(n):
            if state[start] != 0:
                continue

            stack = []
            u = start

            # 1) 따라가며 진행 (미방문 노드만)
            while state[u] == 0:
                state[u] = 1
                idx[u] = len(stack)
                stack.append(u)
                u = edges[u]

            # 2) 사이클 발견 (현재 경로 안에서 다시 만남)
            if state[u] == 1:
                cycle_start = idx[u]
                cycle_len = len(stack) - cycle_start

                # 사이클 노드들은 cycle_len
                for i in range(cycle_start, len(stack)):
                    ans[stack[i]] = cycle_len

                # 사이클 이전 체인은 뒤에서부터 1씩 증가
                for i in range(cycle_start - 1, -1, -1):
                    ans[stack[i]] = ans[edges[stack[i]]] + 1

            # 3) 이미 처리된 노드로 합류한 경우
            else:  # state[u] == 2
                for i in range(len(stack) - 1, -1, -1):
                    ans[stack[i]] = ans[edges[stack[i]]] + 1

            # 4) 마무리
            for v in stack:
                state[v] = 2
                idx[v] = -1

        return ans


class Solution:
    def countVisitedNodes(self, edges: List[int]) -> List[int]:

        n = len(edges)
        d = dict()

        def dfs(cur, visited=[]):
            if cur in d:
                return d[cur] + len(visited)
            if cur in visited:
                cycle = [cur]
                while visited[-1] != cur:
                    cycle.append(visited.pop())
                # print(cycle)
                for elem in cycle:
                    d[elem] = len(cycle)
                return len(cycle) + len(visited) - 1

            return dfs(edges[cur], visited + [cur])

        res = []
        for i in range(n):
            res.append(dfs(i))

        return res
