from typing import List
from heapq import heapify, heappop, heappush

class Solution:
    def getFinalState(self, nums: List[int], k: int, multiplier: int) -> List[int]:
        n = len(nums)
        nums = [(v, i) for i, v in enumerate(nums)]
        heapify(nums)
        for _ in range(k):
            val, index = heappop(nums)
            heappush(nums, (val * multiplier, index))

        arr = [0] * n
        for i in range(n):
            val, index = nums[i]
            arr[index] = val

        return arr
        