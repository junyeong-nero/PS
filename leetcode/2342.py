class Solution:
    def digit_sum(self, num):
        res = 0
        while num > 0:
            res += num % 10
            num //= 10
        return res

    def maximumSum(self, nums: List[int]) -> int:
        seen_sums = defaultdict(list)
        for num in sorted(nums, reverse=True):
            ds = self.digit_sum(num)
            seen_sums[ds].append(num)
        digit_sums = [
            nums[0] + nums[1] if len(nums) > 1 else -1 for nums in seen_sums.values()
        ]
        return max(digit_sums)
