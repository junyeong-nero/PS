class Solution:
    def maximumMedianSum(self, nums: List[int]) -> int:
        n = len(nums) // 3
        nums = sorted(nums)

        # 1 1 1 1 2 2 2 2 3 3 3 3
        # X 1 1 1 2 2 2 2 3 3 + X
        # X X 1 1 2 2 2 2 + X + X
        # X X X 1 2 2 + X + X + X
        # X X X X + X + X + X + X
        #         ^
        #         start with index n, interval 2

        # X : min-max value from selected subsequences
        # + : selected median
        return sum(nums[n : 3 * n : 2])
