from bisect import bisect_left
from typing import List


class Solution:
    def minAbsoluteSumDiff(self, nums1: List[int], nums2: List[int]) -> int:
        MOD = 10**9 + 7

        # 1. nums1을 정렬하여 이분 탐색(Binary Search) 준비
        sorted_nums1 = sorted(nums1)
        n = len(nums1)

        total_diff = 0
        max_decrement = 0

        # 2. 모든 인덱스를 순회하며 "원래 차이" 합산 및 "교체 시 최대 이득" 계산
        for i in range(n):
            original_diff = abs(nums1[i] - nums2[i])
            total_diff += original_diff

            # nums2[i]와 가장 가까운 값을 sorted_nums1에서 찾음
            idx = bisect_left(sorted_nums1, nums2[i])

            # 후보 1: idx 위치의 값 (nums2[i]보다 크거나 같은 값 중 가장 작은 값)
            if idx < n:
                current_diff = abs(sorted_nums1[idx] - nums2[i])
                # 이득 = 원래 차이 - 새로운 차이
                max_decrement = max(max_decrement, original_diff - current_diff)

            # 후보 2: idx - 1 위치의 값 (nums2[i]보다 작은 값 중 가장 큰 값)
            if idx > 0:
                current_diff = abs(sorted_nums1[idx - 1] - nums2[i])
                max_decrement = max(max_decrement, original_diff - current_diff)

        # 3. 전체 합에서 최대 이득을 빼고 MOD 연산
        return (total_diff - max_decrement) % MOD
