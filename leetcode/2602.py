class Solution:
    def minOperations(self, nums: List[int], queries: List[int]) -> List[int]:

        n = len(nums)
        nums = sorted(nums)
        prefix = [0]
        for num in nums:
            prefix.append(prefix[-1] + num)

        res = []
        for query in queries:
            i = bisect_left(nums, query)
            # print(nums, i)
            left = query * (i) - prefix[i]
            right = prefix[-1] - prefix[i] - query * (n - i)

            # print(left, right)
            res.append(left + right)

        return res
