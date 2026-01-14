from typing import List


class Solution:
    def centeredSubarrays(self, nums: List[int]) -> int:
        n = len(nums)
        count = 0

        # i: 부분 배열의 시작 인덱스
        for i in range(n):
            current_sum = 0
            seen = set()  # 현재 부분 배열에 포함된 원소들을 O(1)로 조회하기 위한 집합

            # j: 부분 배열의 끝 인덱스
            for j in range(i, n):
                val = nums[j]

                # 1. 현재 원소를 합에 더함
                current_sum += val

                # 2. 현재 원소를 집합에 추가
                seen.add(val)

                # 3. 부분 배열의 합(current_sum)이
                #    현재 부분 배열의 원소들(seen) 중에 존재하는지 확인
                if current_sum in seen:
                    count += 1

        return count
