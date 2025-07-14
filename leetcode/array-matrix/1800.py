class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        max_sum = 0
        current_sum = 0

        for i, num in enumerate(nums):
            if (
                i > 0 and num <= nums[i - 1]
            ):  # Check if current num is not greater than previous
                current_sum = 0  # Reset current sum if not ascending

            current_sum += num  # Add current number to sum
            max_sum = max(max_sum, current_sum)  # Update max sum

        return max_sum
