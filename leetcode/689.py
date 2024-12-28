from collections import deque
from typing import List

class Solution:
    def maxSumOfThreeSubarrays(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)

        # Calculate the sum of each subarray of length k
        temp = sum(nums[:k])
        arr = [temp]
        for i in range(n - k):
            temp = temp - nums[i] + nums[i + k]
            arr.append(temp)

        m = len(arr)
        res, his = deque(), deque()
        res_v, his_v = 0, 0

        # Depth-first search to find the maximum sum of three subarrays
        def dfs(idx):
            nonlocal his, his_v, res, res_v
            if len(his) >= 3:
                if his_v > res_v:
                    res = his.copy()
                    res_v = his_v
                return

            for i in range(idx + k, m):
                his.append(i)
                his_v += arr[i]
                dfs(i)
                his_v -= arr[i]
                his.pop()

        dfs(-k)
        return list(res)