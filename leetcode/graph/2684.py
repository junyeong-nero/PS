class Solution:
    def maxMoves(self, grid: List[List[int]]) -> int:

        m, n = len(grid), len(grid[0])
        q = list(range(m))
        col_index = 0
        while q:

            # print(q)
            newq = set()
            for index in q:
                if grid[index][col_index] < grid[index][col_index + 1]:
                    newq.add(index)
                if (
                    index - 1 >= 0
                    and grid[index][col_index] < grid[index - 1][col_index + 1]
                ):
                    newq.add(index - 1)
                if (
                    index + 1 < m
                    and grid[index][col_index] < grid[index + 1][col_index + 1]
                ):
                    newq.add(index + 1)

            q = list(newq)
            if not q:
                break

            col_index += 1
            if col_index == n - 1:
                break

        return col_index
