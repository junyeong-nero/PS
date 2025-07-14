from typing import List


class Solution:
    def check(self, nums: List[int]) -> bool:
        """
        Checks if a given list of integers is a rotated sorted array.

        Args:
            nums: A list of integers.

        Returns:
            True if the list is a rotated sorted array, False otherwise.
        """

        inversions = 0  # Count of non-decreasing transitions
        for i in range(len(nums) - 1):
            if nums[i] > nums[i + 1]:
                inversions += 1

        # A rotated sorted array can have at most one "inversion"
        # Check for wrap-around case where first element is greater than last
        return (inversions == 1 and nums[0] >= nums[-1]) or inversions == 0
