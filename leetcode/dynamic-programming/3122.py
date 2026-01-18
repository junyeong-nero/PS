from typing import List
from collections import Counter


class Solution:
    def minimumOperations(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])

        # 1. 각 열(column)별로 숫자(0~9)의 빈도수를 미리 계산합니다.
        # col_counts[j][num] = j번째 열에 있는 숫자 num의 개수
        col_counts = [[0] * 10 for _ in range(n)]
        for row in grid:
            for j, val in enumerate(row):
                col_counts[j][val] += 1

        # 2. DP 테이블 초기화
        # dp[j][num] = j번째 열을 num으로 채웠을 때의 최소 조작 횟수
        # 초기값은 무한대로 설정
        dp = [[float("inf")] * 10 for _ in range(n)]

        # 3. 첫 번째 열(0번 컬럼) 초기화
        for num in range(10):
            # 비용 = 전체 행 개수 - 해당 숫자의 빈도수
            dp[0][num] = m - col_counts[0][num]

        # 4. DP 진행 (1번 컬럼부터 마지막 컬럼까지)
        for j in range(1, n):
            for current_num in range(10):  # 현재 열을 current_num으로 칠할 때
                cost = m - col_counts[j][current_num]

                # 이전 열(j-1)의 가능한 모든 숫자(prev_num)를 확인
                for prev_num in range(10):
                    if current_num == prev_num:
                        continue  # 인접한 열은 같은 숫자일 수 없음

                    # 이전 상태 중 최소값을 현재 비용에 더함
                    dp[j][current_num] = min(
                        dp[j][current_num], dp[j - 1][prev_num] + cost
                    )

        # 5. 마지막 열에서의 최소값이 정답
        return min(dp[n - 1])
