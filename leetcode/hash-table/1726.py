from collections import Counter


class Solution:
    def tupleSameProduct(self, nums: List[int]) -> int:
        """
        Finds the number of tuples (a, b, c, d) such that a * b = c * d,
        where a, b, c, and d are distinct elements from nums.

        Args:
            nums: A list of integers.

        Returns:
            The number of tuples with the same product.
        """
        product_counts = Counter()
        n = len(nums)

        for i in range(n):
            for j in range(i + 1, n):
                product = nums[i] * nums[j]
                product_counts[product] += 1

        total_tuples = 0
        for count in product_counts.values():
            if count >= 2:  # Need at least 2 pairs to form tuples
                # Number of ways to choose 2 pairs from 'count' pairs
                num_pair_combinations = count * (count - 1) // 2
                total_tuples += (
                    num_pair_combinations * 8
                )  # Each pair combination gives 8 tuples

        return total_tuples
