class Solution:
    def minIncrease(self, n: int, edges: List[List[int]], cost: List[int]) -> int:

        graph = defaultdict(set)
        for u, v in edges:
            graph[u].add(v)
            graph[v].add(u)

        visited = set()        

        def dfs(cur):

            visited.add(cur)

            sum_cost = 0
            arr = []
            number_of_nodes = 0

            for node in graph[cur]:
                if node in visited:
                    continue

                temp, temp_cost, temp_nodes = dfs(node)
                sum_cost += temp_cost
                number_of_nodes += temp_nodes
                arr.append(temp)

            # leaf node
            if not arr:
                return cost[cur], 0, 0

            target = max(arr)
            temp = max(arr) * len(arr) - sum(arr)
            if temp > 0:
                sum_cost += temp
                number_of_nodes += len(arr) - arr.count(target)

            return target + cost[cur], sum_cost, number_of_nodes

        res, res_cost, res_nodes = dfs(0)
        return res_nodes