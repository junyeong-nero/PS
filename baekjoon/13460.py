# https://www.acmicpc.net/problem/13460
# 구슬 탈출 2

# 상수 정의
DIRS = [1, 0, -1, 0, 1]  # 방향 벡터 (오른쪽, 아래, 왼쪽, 위)
from collections import deque


def check_position(x, y):
    """좌표가 보드 범위 내에 있는지 확인"""
    return 0 <= x < n and 0 <= y < m


def set_board(pos, tag):
    """보드의 특정 위치에 값을 설정"""
    if not check_position(pos[0], pos[1]):
        return
    board[pos[0]][pos[1]] = tag


def get_board(pos):
    """보드의 특정 위치 값을 반환"""
    if not check_position(pos[0], pos[1]):
        return
    return board[pos[0]][pos[1]]


def move(x, y, dir):
    """구슬을 특정 방향으로 이동"""
    moves = 0
    while check_position(x + DIRS[dir], y + DIRS[dir + 1]) and board[x + DIRS[dir]][y + DIRS[dir + 1]] != '#':
        x += DIRS[dir]
        y += DIRS[dir + 1]
        moves += 1
        if get_board((x, y)) == 'O':
            break
    return x, y, moves


m, n = map(int, input().split())
board = [list(input()) for _ in range(n)]

print(*board, sep='\n')

RED, BLUE = [0, 0], [0, 0]

for i in range(n):
    for j in range(m):
        if board[i][j] == 'R':
            RED = [i, j]
        if board[i][j] == 'B':
            BLUE = [i, j]

print(RED, BLUE)

def bfs():
    queue = deque()
    queue.append((RED[0], RED[1], BLUE[0], BLUE[1], 0))
    visited = set()
    visited.add((RED[0], RED[1], BLUE[0], BLUE[1]))

    while queue:
        rx, ry, bx, by, depth = queue.popleft()
        if depth > 10:
            return -1

        for i in range(4):
            nrx, nry, r_moves = move(rx, ry, i)
            nbx, nby, b_moves = move(bx, by, i)

            if get_board((nbx, nby)) == 'O':
                continue
            if get_board((nrx, nry)) == 'O':
                return depth + 1

            if (nrx, nry) == (nbx, nby):
                if r_moves > b_moves:
                    nrx -= DIRS[i]
                    nry -= DIRS[i + 1]
                else:
                    nbx -= DIRS[i]
                    nby -= DIRS[i + 1]

            if (nrx, nry, nbx, nby) not in visited:
                visited.add((nrx, nry, nbx, nby))
                queue.append((nrx, nry, nbx, nby, depth + 1))

    return -1

print(bfs())
