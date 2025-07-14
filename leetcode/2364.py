from collections import Counter


class Solution:
    def countBadPairs(self, nums: List[int]) -> int:
        """Counts the number of "bad" pairs in the given list.

        A pair (i, j) is considered "bad" if i < j and nums[i] - i != nums[j] - j.

        Args:
            nums: A list of integers.

        Returns:
            The number of bad pairs.
        """

        count = 0  # Initialize the count of bad pairs
        diff_counts = (
            Counter()
        )  # Use a Counter to store the frequency of differences (value - index)

        for index, value in enumerate(nums):
            difference = (
                value - index
            )  # Calculate the difference between the value and index
            count += (
                index - diff_counts[difference]
            )  # Add to the count: current index - number of prior occurrences of this difference
            diff_counts[difference] += 1  # Increment the count of this difference

        return count
