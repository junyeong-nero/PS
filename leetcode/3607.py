class Solution:
    def processQueries(self, c: int, connections: List[List[int]], queries: List[List[int]]) -> List[int]:
        
        graph = defaultdict(list)
        for u, v in connections:
            graph[u].append(v)
            graph[v].append(u)

        power = [True] * c

        def find_smallest_index(cur):
            if power[cur - 1]:
                return cur
            q = deque([cur])
            visited = set()
            while q:
                target = q.popleft()
                visited.add(target)
                neighbors = graph[target]
                for neighbor in neighbors:
                    if neighbor not in visited:
                        q.append(neighbor)
            
            arr = [node for node in visited if power[node - 1]]
            res = min(arr) if arr else -1
            return res

        ans = []
        for types, index in queries:
            if types == 1:
                temp = find_smallest_index(index)
                ans.append(temp)
            elif types == 2:
                power[index - 1] = False

        return ans