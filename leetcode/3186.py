from collections import Counter
from bisect import bisect_left
from typing import List


class Solution:
    def maximumTotalDamage(self, power: List[int]) -> int:
        """
        다이내믹 프로그래밍을 사용하여 최대 총 데미지를 계산합니다.
        keys[i]를 선택했을 때, keys[j] < keys[i] - 2 인
        j까지의 최대 데미지를 O(1)에 찾도록 Prefix Maximum을 활용합니다.
        """

        counter = Counter(power)
        # 1. 키를 정렬합니다.
        keys = sorted(list(counter.keys()))
        n = len(keys)

        # dp[i]: keys[i]를 "선택했을 때" 얻을 수 있는 최대 데미지
        dp = [0] * n

        # max_dp[i]: keys[0]부터 keys[i]까지 고려했을 때 얻을 수 있는 전체 최대 데미지
        # 이 배열을 사용하여 O(1)에 이전 최대 데미지를 찾을 수 있습니다.
        max_dp = [0] * n

        for i in range(n):
            key = keys[i]
            damage = key * counter[key]

            # 2. keys[j] < key - 2 를 만족하는 첫 번째 인덱스(bound)를 찾습니다.
            # bisect_left는 O(log N)
            bound = bisect_left(keys, key - 2)

            # 3. key를 선택했을 때 이전 최대 데미지를 O(1)에 찾습니다.
            prev_max_damage = 0
            if bound > 0:
                # bound - 1 인덱스까지의 최대 데미지 (Prefix Maximum)
                prev_max_damage = max_dp[bound - 1]

            # 4. dp[i] 계산: key를 선택하는 경우
            dp[i] = damage + prev_max_damage

            # 5. max_dp[i] 계산: i번째 키까지의 전체 최대 데미지
            if i == 0:
                max_dp[i] = dp[i]
            else:
                # key를 선택하는 경우(dp[i])와 선택하지 않는 경우(max_dp[i-1]) 중 최대값
                max_dp[i] = max(max_dp[i - 1], dp[i])

        # max_dp의 마지막 원소가 전체 최대 데미지입니다.
        return max_dp[n - 1]
