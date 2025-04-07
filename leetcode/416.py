class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total % 2 == 1:
            return False

        n = len(nums)
        nums.sort()

        prefix = [0]
        for num in nums:
            prefix.append(prefix[-1] + num)

        idx = bisect_left(prefix, total // 2)
        return idx < n and (prefix[idx] == total // 2)