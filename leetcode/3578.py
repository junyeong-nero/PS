from collections import deque
from typing import List


class Solution:
    def countPartitions(self, nums: List[int], k: int) -> int:
        n = len(nums)
        MOD = 10**9 + 7

        # dp[i]는 nums[:i] (첫 i개 원소)를 분할하는 경우의 수
        # dp[0] = 1 (빈 배열을 분할하는 경우 1가지로 초기화)
        dp = [0] * (n + 1)
        dp[0] = 1

        # dp의 누적 합 배열 (구간 합을 빠르게 구하기 위함)
        # presum[i] = dp[0] + ... + dp[i]
        presum = [0] * (n + 1)
        presum[0] = 1

        # 슬라이딩 윈도우 내의 최소/최대 인덱스를 관리할 덱
        min_q = deque()
        max_q = deque()

        left = 0

        for i in range(n):
            # 1. 단조 큐 업데이트 (현재 nums[i]를 윈도우에 포함)

            # 최솟값 큐: 오름차순 유지 (뒤에서부터 현재 값보다 큰 값 제거)
            while min_q and nums[min_q[-1]] >= nums[i]:
                min_q.pop()
            min_q.append(i)

            # 최댓값 큐: 내림차순 유지 (뒤에서부터 현재 값보다 작은 값 제거)
            while max_q and nums[max_q[-1]] <= nums[i]:
                max_q.pop()
            max_q.append(i)

            # 2. 조건(max - min <= k)을 만족하도록 윈도우의 왼쪽(left)을 축소
            while nums[max_q[0]] - nums[min_q[0]] > k:
                left += 1
                # 윈도우 범위를 벗어난 인덱스는 큐에서 제거
                if min_q[0] < left:
                    min_q.popleft()
                if max_q[0] < left:
                    max_q.popleft()

            # 3. DP 전이
            # 현재 원소 nums[i]를 마지막 파티션의 끝으로 할 때,
            # 가능한 시작 지점 j의 범위는 [left, i] 입니다.
            # 따라서 dp[i+1] = sum(dp[left], dp[left+1], ..., dp[i])

            # 누적 합을 이용해 구간 합 계산: presum[i] - presum[left-1]
            current_sum = presum[i]
            if left > 0:
                current_sum = (current_sum - presum[left - 1] + MOD) % MOD

            dp[i + 1] = current_sum

            # 누적 합 갱신
            presum[i + 1] = (presum[i] + dp[i + 1]) % MOD

        return dp[n]
