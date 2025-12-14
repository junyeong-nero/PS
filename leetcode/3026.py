from typing import List
import math


class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        n = len(nums)
        # 결과값 초기화 (음수가 답일 수도 있으므로 -inf 사용)
        res = -math.inf

        # 현재까지의 누적 합
        current_prefix_sum = 0

        # key: 숫자(num), value: 해당 숫자가 처음 등장하기 직전의 최소 누적 합 (min_prefix)
        # 즉, 이 맵은 '시작점' 후보들을 관리합니다.
        min_prefix = {}

        for num in nums:
            # 1. 조건에 맞는 이전 인덱스(시작점) 찾기
            # 현재 숫자가 num일 때, 시작 숫자는 (num - k) 또는 (num + k) 여야 함

            # Case A: 시작 숫자가 num - k 인 경우
            target1 = num - k
            if target1 in min_prefix:
                # 부분 배열 합 = (현재까지 누적합 + num) - (target1 직전까지의 누적합)
                # 여기서 current_prefix_sum은 num을 더하기 전 상태이므로 + num을 해줍니다.
                subarray_sum = current_prefix_sum + num - min_prefix[target1]
                res = max(res, subarray_sum)

            # Case B: 시작 숫자가 num + k 인 경우
            target2 = num + k
            if target2 in min_prefix:
                subarray_sum = current_prefix_sum + num - min_prefix[target2]
                res = max(res, subarray_sum)

            # 2. 현재 숫자에 대한 누적 합 정보 업데이트 (다음에 누군가의 시작점이 되기 위해)
            # 우리는 (current_prefix_sum)을 저장해야 합니다. (num이 시작점이 될 때 뺄셈에 사용될 값)
            if num not in min_prefix or current_prefix_sum < min_prefix[num]:
                min_prefix[num] = current_prefix_sum

            # 다음 루프를 위해 현재 숫자를 누적 합에 더함
            current_prefix_sum += num

        # 문제 요구사항: 유효한 부분 배열이 없으면 0 반환
        return 0 if res == -math.inf else res
