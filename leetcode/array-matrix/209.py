class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:

        prefix = [0]
        for num in nums:
            prefix.append(prefix[-1] + num)
        # print(prefix)

        n = len(prefix)
        i, j = 0, 0
        res = float("inf")

        while i <= j < n:
            if prefix[j] - prefix[i] >= target:
                # print(j, i, prefix[j] - prefix[i])
                res = min(res, j - i)
                i += 1
            else:
                j += 1

        return 0 if res == float("inf") else res
