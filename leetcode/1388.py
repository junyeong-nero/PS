from typing import List


class Solution:
    def maxSizeSlices(self, slices: List[int]) -> int:
        m = len(slices)
        n = m // 3

        # maxSum 함수: 선형 배열에서 인접하지 않게 n개를 뽑았을 때의 최대 합
        def maxSum(arr, n):
            m_arr = len(arr)
            # dp[i][j]: arr의 앞에서부터 i개의 요소를 고려하여 j개를 선택했을 때의 최대 합
            # 초기화: (m_arr + 1) x (n + 1) 크기의 0으로 채워진 2차원 리스트
            dp = [[0] * (n + 1) for _ in range(m_arr + 1)]

            for i in range(1, m_arr + 1):
                for j in range(1, n + 1):
                    if i == 1:
                        # 배열에 요소가 하나뿐이라면 그 하나를 선택
                        dp[i][j] = arr[0]
                    else:
                        # 점화식:
                        # 1. 이번 요소(arr[i-1])를 선택하지 않음 -> dp[i-1][j]
                        # 2. 이번 요소를 선택함 -> 두 칸 전의 상태에서 j-1개를 선택한 값 + 현재 값 (dp[i-2][j-1] + arr[i-1])
                        dp[i][j] = max(dp[i - 1][j], dp[i - 2][j - 1] + arr[i - 1])

            return dp[m_arr][n]

        # 원형 배열의 특성상 첫 번째와 마지막 요소가 인접해 있음.
        # 따라서 문제를 두 가지 선형 배열 문제로 나누어 풂:

        # Case 1: 첫 번째 요소를 포함할 가능성이 있음 (마지막 요소는 무조건 제외) -> slices[0 : m-1]
        slices1 = slices[:-1]

        # Case 2: 마지막 요소를 포함할 가능성이 있음 (첫 번째 요소는 무조건 제외) -> slices[1 : m]
        slices2 = slices[1:]

        # 두 경우 중 더 큰 값을 반환
        return max(maxSum(slices1, n), maxSum(slices2, n))
