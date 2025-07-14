class Solution:
    def countBattleships(self, board: List[List[str]]) -> int:

        m, n = len(board), len(board[0])

        def check(sx, sy):
            x, y = sx, sy
            dirs = [1, 0, -1, 0, 1]
            for i in range(4):
                dx, dy = dirs[i], dirs[i + 1]
                while 0 <= x + dx < m and 0 <= y + dy < n:
                    nx, ny = x + dx, y + dy
                    if board[nx][ny] == "X":
                        board[nx][ny] = "."
                        x, y = nx, ny
                    else:
                        break

        count = 0
        for i in range(m):
            for j in range(n):
                if board[i][j] == ".":
                    continue
                count += 1
                check(i, j)

        return count
