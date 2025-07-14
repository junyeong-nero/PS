from typing import List


class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        """
        Finds the length of the longest monotonic (either increasing or decreasing) subarray in a list of numbers.

        Args:
            nums: A list of integers.

        Returns:
            The length of the longest monotonic subarray.
        """

        if not nums:
            return 0

        max_len = 1  # Initialize max length to 1 (a single element is always monotonic)

        # Helper function to check for a specific type of monotonicity and update max_len
        def check_monotonic(is_increasing: bool) -> None:
            nonlocal max_len
            current_len = 1
            for i in range(len(nums) - 1):
                if (is_increasing and nums[i] < nums[i + 1]) or (
                    not is_increasing and nums[i] > nums[i + 1]
                ):
                    current_len += 1
                else:
                    current_len = 1  # Reset if the monotonic pattern breaks
                max_len = max(max_len, current_len)

        check_monotonic(True)  # Check for increasing
        check_monotonic(False)  # Check for decreasing

        return max_len
