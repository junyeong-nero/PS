from typing import List


class Solution:
    def findMaxFish(self, grid: List[List[int]]) -> int:
        """
        Finds the maximum number of fish that can be caught by traversing connected cells in a grid.

        Args:
            grid: A 2D list of integers representing the grid, where each cell contains the number of fish.

        Returns:
            The maximum number of fish that can be caught from a connected component.
        """

        rows = len(grid)
        cols = len(grid[0]) if rows > 0 else 0  # Handle edge case of empty grid

        def dfs(row: int, col: int) -> int:
            """
            Depth-first search to explore connected cells and sum the fish.

            Args:
                row: The current row index.
                col: The current column index.

            Returns:
                The total fish count of the connected component.
            """
            if row < 0 or row >= rows or col < 0 or col >= cols or grid[row][col] == 0:
                return 0

            fish_count = grid[row][col]
            grid[row][col] = 0  # Mark cell as visited
            fish_count += dfs(row + 1, col)  # Down
            fish_count += dfs(row - 1, col)  # Up
            fish_count += dfs(row, col + 1)  # Right
            fish_count += dfs(row, col - 1)  # Left

            return fish_count

        max_fish = 0
        for row in range(rows):
            for col in range(cols):
                max_fish = max(max_fish, dfs(row, col))

        return max_fish
