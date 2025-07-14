class Solution:
    def checkLine(self, line: list[str]) -> bool:
        seen = set()
        for c in line:
            if c != ".":
                if c in seen:
                    return False
                seen.add(c)
        return True

    def checkSection(self, board: list[list[str]], i: int, j: int) -> bool:
        seen = set()
        for a in range(3 * i, 3 * (i + 1)):
            for b in range(3 * j, 3 * (j + 1)):
                c = board[a][b]
                if c != ".":
                    if c in seen:
                        return False
                    seen.add(c)
        return True

    def isValidSudoku(self, board: list[list[str]]) -> bool:
        # check horizontal lines
        for row in board:
            if not self.checkLine(row):
                return False

        # check vertical lines
        for j in range(len(board[0])):
            column = [board[i][j] for i in range(len(board))]
            if not self.checkLine(column):
                return False

        # check sections
        for i in range(3):
            for j in range(3):
                if not self.checkSection(board, i, j):
                    return False

        return True
