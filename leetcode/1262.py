class Solution:
    def maxSumDivThree(self, nums: List[int]) -> int:
        n = len(nums)
        d = defaultdict(list)
        nums = sorted(nums, reverse=True)
        for num in nums:
            d[num % 3].append(num)

        tot = sum(nums)
        remove = float("inf")
        if tot % 3 == 0:
            remove = 0
        elif tot % 3 == 1:
            if len(d[1]) >= 1:
                remove = min(remove, d[1][-1])
            if len(d[2]) >= 2:
                remove = min(remove, d[2][-2] + d[2][-1])
        else:
            if len(d[1]) >= 2:
                remove = min(remove, d[1][-2] + d[1][-1])
            if len(d[2]) >= 1:
                remove = min(remove, d[2][-1])

        return tot - remove
