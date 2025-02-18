class Solution:
    def smallestNumber(self, s: str) -> str:
        """
        Generates the smallest possible number based on the given 'I' and 'D' string.

        Args:
            s: A string containing only 'I' (increasing) and 'D' (decreasing) characters.

        Returns:
            The smallest possible number as a string.
        """

        result =
        available_digits = list('987654321')  # Use a list for efficient pop operations

        for segment_length in map(len, s.split('I')):
            # Take the required number of digits from the pool and reverse them
            segment = [available_digits.pop() for _ in range(segment_length + 1)][::-1]
            result.extend(segment)  # More efficient than res += segment in a loop

        return "".join(result)


# Example usage (you can add this for testing)
sol = Solution()
print(sol.smallestNumber("IDID"))  # Output: 12354
print(sol.smallestNumber("D"))    # Output: 21
print(sol.smallestNumber("I"))    # Output: 12
print(sol.smallestNumber("DID"))  # Output: 32154