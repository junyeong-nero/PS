class Solution:
    def numMagicSquaresInside(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])

        def is_magic(r: int, c: int) -> bool:
            # 1. 중앙값이 5가 아니면 3x3 마법진이 될 수 없음 (수학적 특징)
            if grid[r + 1][c + 1] != 5:
                return False

            # 2. 1부터 9까지의 숫자가 중복 없이 포함되어 있는지 확인
            vals = [grid[r + i][c + j] for i in range(3) for j in range(3)]
            if sorted(vals) != list(range(1, 10)):
                return False

            # 3. 행, 열, 대각선의 합이 모두 15인지 확인
            # 행(Rows)
            for i in range(3):
                if sum(grid[r + i][c : c + 3]) != 15:
                    return False

            # 열(Columns)
            for j in range(3):
                if grid[r][c + j] + grid[r + 1][c + j] + grid[r + 2][c + j] != 15:
                    return False

            # 대각선(Diagonals)
            if grid[r][c] + grid[r + 2][c + 2] != 10:
                return False  # 5(중앙) 제외 양끝 합
            if grid[r][c + 2] + grid[r + 2][c] != 10:
                return False

            return True

        count = 0
        # 3x3 격자를 만들 수 있는 범위만 탐색
        for r in range(rows - 2):
            for c in range(cols - 2):
                if is_magic(r, c):
                    count += 1
        return count
