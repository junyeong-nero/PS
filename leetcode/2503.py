class Solution:
    def maxPoints(self, grid: List[List[int]], queries: List[int]) -> List[int]:
        m, n = len(grid), len(grid[0])
        # queries[i] > current -> move

    
        visited = {(0, 0)}
        border = {(0, 0)}

        def func(query):
            nonlocal visited, border

            q = deque(border)
            new_border = set()
            while q:
                x, y = q.popleft()
                dirs = [1, 0, -1, 0, 1]
                for i in range(4):
                    nx = x + dirs[i]
                    ny = y + dirs[i + 1]
                    if nx < 0 or nx >= m or ny < 0 or ny >= n:
                        continue
                    if grid[nx][ny] >= query:
                        new_border.add((x, y))
                        continue
                    if (nx, ny) in visited:
                        continue

                    visited.add((nx, ny))
                    q.append((nx, ny))

            border = new_border
            return len(visited)
        
        d = dict()
        for query in sorted(set(queries)):
            temp = 0 if grid[0][0] >= query else func(query)
            d[query] = temp

        # print(d)
        
        return [d[query] for query in queries]

                    
