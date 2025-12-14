class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        n = len(nums)
        d = defaultdict(list)

        prefix = [0]
        for num in nums:
            prefix.append(prefix[-1] + num)

        for i, num in enumerate(nums):
            d[num].append(i)

        def help(idx):
            cur = nums[idx]
            res = float("-inf")

            start = bisect_left(d[cur - k], idx)
            end = len(d[cur - k])
            for i in range(start, end):
                j = d[cur - k][i]
                res = max(res, prefix[j + 1] - prefix[idx])

            start = bisect_left(d[cur + k], idx)
            end = len(d[cur + k])
            for i in range(start, end):
                j = d[cur + k][i]
                res = max(res, prefix[j + 1] - prefix[idx])

            return res

        res = float("-inf")
        for i in range(n):
            res = max(res, help(i))

        return 0 if res == float("-inf") else res
