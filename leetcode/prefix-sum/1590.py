class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        n = len(nums)
        mod = sum(nums) % p
        if mod == 0:
            return 0
        # find sum(subarray) % p = mod

        prefix = [0]
        for num in nums:
            prefix.append(prefix[-1] + num)

        res = float("inf")
        d = dict()
        for i in range(n + 1):
            temp = prefix[i] % p
            # prefix[i] - prefix[j] = mod
            # prefix[j] = (preifx[i] - mod + p) % p

            j = (temp - mod + p) % p
            res = min(res, i - d.get(j, -float("inf")))
            d[temp] = i

        return -1 if res >= n else res
