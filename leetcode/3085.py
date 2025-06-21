from collections import Counter

class Solution:
    def minimumDeletions(self, word: str, k: int) -> int:
        """
        Calculates the minimum number of deletions to make the word "beautiful".

        A word is considered beautiful if the frequency of each character `char_freq`
        satisfies `min_freq <= char_freq <= min_freq + k`.

        Args:
            word: The input string.
            k: The maximum allowed difference between the maximum and minimum
               character frequencies.

        Returns:
            The minimum number of deletions required.
        """
        char_counts = Counter(word)
        frequencies = sorted(list(char_counts.values()))
        n = len(frequencies)
        min_deletions = float('inf')

        # Calculate prefix sums for efficient range sum queries
        prefix_sum = [0] * (n + 1)
        for i in range(n):
            prefix_sum[i + 1] = prefix_sum[i] + frequencies[i]

        # Iterate through all possible ranges [frequencies[i], frequencies[j]]
        # which represent the potential min_freq and max_freq within the k constraint
        for i in range(n):
            for j in range(i, n):
                diff = frequencies[j] - frequencies[i]
                if diff <= k:
                    # Calculate deletions for characters with frequency < frequencies[i]
                    deletions_left = prefix_sum[i]

                    # Calculate deletions for characters with frequency > frequencies[i] + k
                    deletions_right = 0
                    for x in range(j + 1, n):
                        deletions_right += max(0, frequencies[x] - (frequencies[i] + k))
                    
                    min_deletions = min(min_deletions, deletions_left + deletions_right)
            
        return min_deletions if min_deletions != float('inf') else 0