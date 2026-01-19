from typing import List


class Solution:
    def maxSideLength(self, mat: List[List[int]], threshold: int) -> int:
        m, n = len(mat), len(mat[0])

        # 1. 2D Prefix Sum 배열 생성 (Padding을 1칸 주어 인덱스 계산 단순화)
        # P[i][j]는 (0,0)부터 (i-1, j-1)까지의 합을 저장
        P = [[0] * (n + 1) for _ in range(m + 1)]

        for r in range(1, m + 1):
            for c in range(1, n + 1):
                # 점화식: 위쪽 합 + 왼쪽 합 - 대각선 위 중복 합 + 현재 값
                P[r][c] = (
                    P[r - 1][c] + P[r][c - 1] - P[r - 1][c - 1] + mat[r - 1][c - 1]
                )

        def get_sum(r1, c1, r2, c2):
            """(r1, c1)에서 (r2, c2)까지의 부분 합 반환 (0-based index 입력)"""
            # Prefix Sum 배열은 1-based index이므로 +1 보정 필요
            return P[r2 + 1][c2 + 1] - P[r1][c2 + 1] - P[r2 + 1][c1] + P[r1][c1]

        max_side = 0

        # 2. 행렬을 한 번만 순회 (Bottom-Right 기준)
        for r in range(m):
            for c in range(n):
                # 우리가 확인하고 싶은 길이는 현재 찾은 최대 길이보다 1 큰 값
                target_len = max_side + 1

                # 현재 위치(r, c)가 우측 하단일 때, target_len만큼 뒤로 갈 수 있는지(범위) 체크
                if r - target_len + 1 >= 0 and c - target_len + 1 >= 0:
                    # 해당 정사각형의 합 계산
                    # Top-Left 좌표: (r - target_len + 1, c - target_len + 1)
                    # Bottom-Right 좌표: (r, c)
                    current_sum = get_sum(r - target_len + 1, c - target_len + 1, r, c)

                    if current_sum <= threshold:
                        max_side += 1

        return max_side
