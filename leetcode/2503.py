from queue import PriorityQueue

class Solution:
    def maxPoints(self, grid, queries):
        rows, cols = len(grid), len(grid[0])  # Get the dimensions of the grid
        DIRECTIONS = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # Define the possible directions to move (right, down, left, up)
        
        sorted_queries = sorted([(val, idx) for idx, val in enumerate(queries)])  # Sort queries by value, keeping track of original indices
        result = [0] * len(queries)  # Initialize the result array with zeros
        
        heap = PriorityQueue()  # Initialize a priority queue to store cells to visit, ordered by their values
        visited = [[False] * cols for _ in range(rows)]  # Initialize a 2D array to track visited cells
        
        heap.put((grid[0][0], 0, 0))  # Add the starting cell (top-left) to the heap
        visited[0][0] = True  # Mark the starting cell as visited
        points = 0  # Initialize the number of points to 0
        
        for query_val, query_idx in sorted_queries:  # Iterate through the sorted queries
            while not heap.empty() and heap.queue[0][0] < query_val:  # While the heap is not empty and the smallest cell value is less than the current query value
                _, row, col = heap.get()  # Get the cell with the smallest value from the heap
                points += 1  # Increment the points count
                
                for dr, dc in DIRECTIONS:  # Iterate through the possible directions
                    nr, nc = row + dr, col + dc  # Calculate the coordinates of the neighboring cell
                    if (0 <= nr < rows and 0 <= nc < cols and 
                        not visited[nr][nc]):  # If the neighbor is within the grid bounds and not visited
                        heap.put((grid[nr][nc], nr, nc))  # Add the neighbor to the heap
                        visited[nr][nc] = True  # Mark the neighbor as visited
            
            result[query_idx] = points  # Store the current points count in the result array at the original query index
        
        return result  # Return the result array