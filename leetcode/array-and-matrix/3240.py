class Solution:
    def minFlips(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        res = 0  # minimum changes required in 4 way symmetry
        single = 0  # number of (1, 0) pair in a 2 way symmetry
        double = 0  # number of (1, 1) pair in a 2 way symmetry

        # Process 4-way symmetry
        for i in range(m // 2):
            for j in range(n // 2):
                # Change to all 1s or all 0s
                ones = (
                    grid[i][j]
                    + grid[i][n - 1 - j]
                    + grid[m - 1 - i][j]
                    + grid[m - 1 - i][n - 1 - j]
                )
                res += min(ones, 4 - ones)

            # Process the middle column if it exists (2-way symmetry)
            if n % 2 == 1:
                ones = grid[i][n // 2] + grid[m - 1 - i][n // 2]
                single += ones == 1  # (1, 0)
                double += ones == 2  # (1, 1)

        # Process the middle row if it exists (2-way symmetry)
        if m % 2 == 1:
            for j in range(n // 2):
                ones = grid[m // 2][j] + grid[m // 2][n - 1 - j]
                single += ones == 1  # (1, 0)
                double += ones == 2  # (1, 1)
            if n % 2 == 1:
                res += grid[m // 2][n // 2]  # Center cell needs to be 0 if it's 1

        # Adjust based on the number of (1, 1) pairs:
        # 1. If even, the total number of 1s is already a multiple of 4.
        #    We can change every (1, 0) pair to (0, 0) if there's any.
        # 2. If odd, but we have (1, 0) pairs, convert one (1, 0) to (1, 1).
        if double % 2 == 0 or single > 0:
            return res + single

        # 3. If the number of (1, 1) pairs is odd and there are no (1, 0) pairs,
        #    flip one (1, 1) pair to (0, 0).
        return res + 2
