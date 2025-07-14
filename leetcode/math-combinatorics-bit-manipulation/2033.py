class Solution:
    def minOperations(self, grid: List[List[int]], x: int) -> int:
        m, n = len(grid), len(grid[0])

        MOD = grid[0][0] % x
        arr = []

        for i in range(m):
            for j in range(n):
                mod = grid[i][j] % x
                if mod != MOD:
                    return -1
                arr.append(grid[i][j])

        arr.sort()
        median = arr[len(arr) // 2]

        total_operations = 0
        for num in arr:
            total_operations += abs(num - median) // x

        return total_operations
