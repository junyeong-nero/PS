class Solution:
    def maxPoints(self, grid: List[List[int]], queries: List[int]) -> List[int]:
        m, n = len(grid), len(grid[0])
        # queries[i] > current -> move
        
        def func(query):
            if grid[0][0] >= query:
                return 0

            area = 0
            visited = {(0, 0)}
            q = deque([(0, 0)])
            while q:
                x, y = q.popleft()
                area += 1

                dirs = [1, 0, -1, 0, 1]
                for i in range(4):
                    nx = x + dirs[i]
                    ny = y + dirs[i + 1]
                    if nx < 0 or nx >= m or ny < 0 or ny >= n:
                        continue
                    if (nx, ny) in visited or grid[nx][ny] >= query:
                        continue

                    visited.add((nx, ny))
                    q.append((nx, ny))

            return area
        
        return [func(query) for query in queries]

                    
