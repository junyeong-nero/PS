from typing import List
from functools import cache


class Solution:
    def minimumValueSum(self, nums: List[int], andValues: List[int]) -> int:
        n = len(nums)
        m = len(andValues)

        @cache
        def dfs(i: int, j: int, current_and: int) -> int:
            # 기저 사례 1: 모든 배열과 타겟을 다 처리했을 때 성공
            if i == n and j == m:
                return 0
            # 기저 사례 2: 배열이나 타겟 중 하나만 먼저 끝난 경우 실패
            if i == n or j == m:
                return float("inf")

            # 새로운 AND 값 계산
            # current_and가 -1이면 새로운 부분 배열의 시작이므로 nums[i]를 그대로 씀
            new_and = nums[i] if current_and == -1 else current_and & nums[i]
            target = andValues[j]

            # 가지치기 (Pruning):
            # new_and가 target보다 작아지거나(비트 소실), target이 갖고 있는 비트를 잃어버린 경우
            # AND 연산은 비트를 0으로만 만들 수 있으므로 영원히 복구 불가능 -> 즉시 종료
            if (new_and & target) < target:
                return float("inf")

            res = float("inf")

            # 경우 1: 현재 AND 값이 타겟과 일치한다면, 여기서 부분 배열을 끊을 수 있음
            if new_and == target:
                # 현재 값을 더하고, 다음 부분 배열 탐색 (새 시작이므로 current_and를 -1로 전달)
                val = dfs(i + 1, j + 1, -1)
                if val != float("inf"):
                    res = nums[i] + val

            # 경우 2: 현재 상태에서 끊지 않고 다음 숫자로 계속 진행 (배열 확장)
            # 단, 이 경우에도 DP를 통해 중복 연산을 방지함
            res = min(res, dfs(i + 1, j, new_and))

            return res

        # 초기 호출: current_and는 -1 (아직 아무것도 선택 안 함을 의미)
        res = dfs(0, 0, -1)
        return -1 if res == float("inf") else res
