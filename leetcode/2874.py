class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        n = len(nums)

        # max : nums[i]
        # min : nums[j]
        # max : nums[k]

        # min : nums[i]
        # max : nums[j] > 0
        # min : nums[k] < 0

        a = b = nums[0]
        c = d = 0
        res = 0

        for num in nums[1:]:

            res = max(res, c * num)
            res = max(res, d * num)

            c = max(c, a - num)
            d = min(d, b - num)

            a = max(a, num)
            b = min(b, num)

        return res
