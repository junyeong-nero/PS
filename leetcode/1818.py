import sys
from bisect import bisect_left
from typing import List

# 1. 재귀 깊이 제한을 대폭 늘립니다 (N=100,000 대응)
sys.setrecursionlimit(200000)


class Solution:
    def minAbsoluteSumDiff(self, nums1: List[int], nums2: List[int]) -> int:
        n = len(nums1)
        MOD = 10**9 + 7

        # 이분 탐색을 위한 정렬된 nums1
        pool = sorted(nums1)

        # 2. 미리 남은 구간의 원래 차이 합(Suffix Sum)을 구해둡니다.
        # suffix_sum[i] = i번째 인덱스부터 끝까지의 원래 차이 합
        # 이렇게 하면 '이미 교체를 수행한 이후'에는 재귀를 더 들어갈 필요가 없습니다.
        suffix_sum = [0] * (n + 1)
        for i in range(n - 1, -1, -1):
            suffix_sum[i] = suffix_sum[i + 1] + abs(nums1[i] - nums2[i])

        # 메모이제이션 (인덱스만 키로 사용)
        # dfs(i)는 "i번째 인덱스부터 끝까지, 아직 교체 기회를 안 썼을 때의 최소 합"을 의미
        memo = {}

        def find_best_diff(target):
            """target(nums2[i])과 pool에서 가장 가까운 값의 차이를 반환"""
            idx = bisect_left(pool, target)
            best_diff = float("inf")

            # idx 위치 확인 (target보다 크거나 같은 값 중 최소)
            if idx < n:
                best_diff = min(best_diff, abs(pool[idx] - target))
            # idx-1 위치 확인 (target보다 작은 값 중 최대)
            if idx > 0:
                best_diff = min(best_diff, abs(pool[idx - 1] - target))
            return best_diff

        def dfs(i):
            # 기저 조건: 끝에 도달하면 0 반환
            if i == n:
                return 0

            if i in memo:
                return memo[i]

            original_diff = abs(nums1[i] - nums2[i])

            # 선택 1: 이번 위치(i)에서 교체하지 않고 다음으로 넘어감
            # 비용 = 원래 차이 + 나머지 구간의 최소 합
            res = original_diff + dfs(i + 1)

            # 선택 2: 이번 위치(i)에서 교체함 (단, 처음이자 마지막 기회 사용)
            # 비용 = 교체 후 차이 + 나머지 구간은 원래 합 그대로(suffix_sum 사용)
            replaced_diff = find_best_diff(nums2[i])
            res_if_swapped = replaced_diff + suffix_sum[i + 1]

            # 두 경우 중 더 작은 값 선택
            res = min(res, res_if_swapped)

            memo[i] = res
            return res

        # DFS 시작
        return dfs(0) % MOD
