from typing import List


class Solution:
    def minimumOperations(self, nums: List[int], target: List[int]) -> int:
        n = len(nums)
        # incr: 이전 인덱스에서 이어져 온 '증가' 연산의 양
        # decr: 이전 인덱스에서 이어져 온 '감소' 연산의 양 (음수 값으로 유지)
        # ops: 총 연산 횟수
        incr = decr = ops = 0

        for i in range(n):
            # 목표값과 현재값의 차이 (양수면 증가 필요, 음수면 감소 필요)
            diff = target[i] - nums[i]

            if diff > 0:
                # 1. 양수 차이 (증가시켜야 하는 경우)

                # 이전 단계의 증가량(incr)보다 현재 필요한 증가량(diff)이 더 크다면,
                # 그 차이만큼 새로운 연산을 추가해야 함.
                # (예: 이전에 +2만큼 올리고 있었는데, 여기선 +5가 필요하면 +3만큼 더 올려야 함)
                if incr < diff:
                    ops += diff - incr

                # 현재의 차이를 다음 인덱스를 위한 '증가량'으로 업데이트
                incr = diff
                # 부호가 바뀌었으므로 감소량(decr)은 초기화
                decr = 0

            elif diff < 0:
                # 2. 음수 차이 (감소시켜야 하는 경우)

                # 이전 단계의 감소량(decr)보다 현재 필요한 감소량(diff)이 더 작다면(더 큰 음수라면),
                # 더 많이 깎아야 하므로 그 차이만큼 연산 추가.
                # (예: 이전에 -2였는데, 여기선 -5가 필요하면 3만큼 더 깎는 연산 필요)
                if diff < decr:
                    ops += decr - diff

                # 현재의 차이를 다음 인덱스를 위한 '감소량'으로 업데이트
                decr = diff
                # 부호가 바뀌었으므로 증가량(incr)은 초기화
                incr = 0

            else:
                # 3. 차이가 0인 경우 (이미 목표값과 같음)
                # 연속된 연산이 끊기므로 둘 다 초기화
                incr = decr = 0

        return ops
