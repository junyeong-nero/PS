from typing import List
from itertools import accumulate


class Solution:
    def stoneGameVII(self, stones: List[int]) -> int:
        """
        Calculates the maximum score difference between Alice and Bob in the Stone Game VII using dynamic programming.

        Args:
            stones: A list of integers representing the values of the stones.

        Returns:
            The maximum score difference between Alice and Bob if they both play optimally.
        """
        n = len(stones)

        # Initialize a 2D DP table to store the maximum score difference
        dp = [[0] * n for _ in range(n)]

        # Calculate prefix sums for efficient range sum calculations
        prefix_sums = [0] + list(accumulate(stones))

        # Iterate through the DP table diagonally (bottom-up)
        for i in range(n - 2, -1, -1):  # Start from second-to-last row to first row
            for j in range(i + 1, n):  # Start from column after i to last column
                # dp[i][j] represents the max score difference between Alice and Bob
                # when considering the subarray stones[i:j+1]
                dp[i][j] = max(
                    prefix_sums[j + 1]
                    - prefix_sums[i + 1]
                    - dp[i + 1][j],  # Alice takes left stone
                    prefix_sums[j]
                    - prefix_sums[i]
                    - dp[i][j - 1],  # Alice takes right stone
                )

        # The maximum score difference is stored at dp[0][n-1] (whole stones array)
        return dp[0][n - 1]
