from typing import List
from itertools import accumulate
from bisect import bisect_left, bisect_right
from heapq import heapify, heappop, heappush

class Solution:
    def minimumSize(self, nums: List[int], maxOperations: int) -> int:
        prefix = []
        for num in nums:
            prefix.append(prefix[-1] + num)
        


res = Solution().maxCount()