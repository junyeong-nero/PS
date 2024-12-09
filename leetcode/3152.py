# https://leetcode.com/problems/special-array-ii/

from typing import List
from bisect import bisect_left, bisect_right

class Solution:
    def isArraySpecial(self, nums: List[int], queries: List[List[int]]) -> List[bool]:
        nums = [x % 2 for x in nums]
        res = []
        prev = -1
        for i in range(len(nums)):
            cur = nums[i]
            if prev == cur:
                res.append(i)
            prev = cur

        # print(res)

        def help(query):
            index = bisect_left(res, query[1])
            t1 = (index < len(res) and query[0] < res[index] and res[index] <= query[1])
            index = bisect_right(res, query[0])
            t2 = (index < len(res) and query[0] < res[index] and res[index] <= query[1])
            return not (t1 or t2)

        return [help(q) for q in queries]
    
    # prefix sum version
    def isArraySpecial(
        self, nums: List[int], queries: List[List[int]]
    ) -> List[bool]:
        ans = [False] * len(queries)
        prefix = [0] * len(nums)
        prefix[0] = 0

        for i in range(1, len(nums)):
            if nums[i] % 2 == nums[i - 1] % 2:
                # new violative index found
                prefix[i] = prefix[i - 1] + 1
            else:
                prefix[i] = prefix[i - 1]

        for i in range(len(queries)):
            query = queries[i]
            start = query[0]
            end = query[1]

            ans[i] = prefix[end] - prefix[start] == 0

        return ans