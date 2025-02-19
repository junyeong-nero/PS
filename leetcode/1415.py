from functools import cache

class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        """
        Generates the k-th lexicographically happy string of length n.

        A happy string is a string that consists only of the letters 'a', 'b', and 'c',
        and no two adjacent characters are the same.

        Args:
            n: The desired length of the happy string.
            k: The k-th lexicographical happy string to return.

        Returns:
            The k-th lexicographical happy string of length n, or an empty string if it doesn't exist.
        """

        count = 0
        result = ""  # More descriptive variable name

        @cache  # Use lru_cache for potential performance benefits if needed
        def find_happy_string(current_string):
            nonlocal count, result

            if len(current_string) == n:
                count += 1
                if count == k:
                    result = current_string
                return

            for next_char in "abc":
                if current_string and next_char == current_string[-1]:
                    continue
                find_happy_string(current_string + next_char)

        find_happy_string("")
        return result