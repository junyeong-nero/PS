class Solution:
    def minOperations(self, nums: List[int]) -> int:
        n = len(nums)
        set_nums = set(nums)
        if not nums or n == 0 or set_nums == {0}:
            return 0
        if len(set_nums) == 1:
            return 1

        min_value = min(nums)
        res = 0
        if min_value > 0:
            res += 1
            for i in range(n):
                if nums[i] == min_value:
                    nums[i] = 0

        boundary = [[n + 1, -1]]
        for i in range(n):
            if nums[i] == 0:
                boundary.append([n + 1, -1])
                continue

            boundary[-1][0] = min(boundary[-1][0], i)
            boundary[-1][1] = max(boundary[-1][1], i)

        for bound in boundary:
            subset = nums[bound[0] : bound[1] + 1]
            res += self.minOperations(subset)

        return res
