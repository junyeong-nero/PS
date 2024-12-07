from heapq import heapify, heappop, heappush
from typing import List

class Solution:
    def minimumSize(self, nums: List[int], maxOperations: int) -> int:
        # 이진 탐색 범위: 최소 1, 최대 max(nums)
        left, right = 1, max(nums)

        while left < right:
            mid = (left + right) // 2
            operations = 0

            for num in nums:
                # 각 num을 mid 이하로 만들기 위해 필요한 연산 수 계산
                operations += (num - 1) // mid

            # 필요한 연산 수가 maxOperations 이하라면, penalty를 줄여볼 수 있음
            if operations <= maxOperations:
                right = mid
            else:
                left = mid + 1

        return left


# class Solution:
#     def minimumSize(self, nums: List[int], maxOperations: int) -> int:
        
#         arr = [-x for x in nums]
#         heapify(arr)

#         while maxOperations > 0:
#             tar = -heappop(arr)
#             print(tar)
            
#             num = -float('inf')
#             if len(arr) > 0:
#                 num = -heappop(arr)
#                 heappush(arr, -num)

#             for i in range(2, maxOperations + 2):
#                 if tar / i <= num:
#                     maxOperations -= (i - 1)
#                     break
#             # print(i)

#             temp = 0
#             for _ in range(i - 1):
#                 heappush(arr, -(tar // i))
#                 temp += tar // i
#             heappush(arr, -(tar - temp))

#         return -heappop(arr)